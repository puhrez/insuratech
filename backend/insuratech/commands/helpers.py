# -*- coding: utf-8 -*-
"""
    commands.helpers
    ~~~~~~~~~~~~~~
    helpers for commands
"""
import mmh3
import pandas
from datetime import datetime
from multiprocessing import Pool
from functools import partial
from math import ceil
from flask import current_app
from sqlalchemy.exc import ProgrammingError
from insuratech.core import db


def add_hash(row):
    row['hash'] = mmh3.hash(str(row.values))
    return row


def get_ids(key, table):
    try:
        ids = set(x[0] for x in db.session.execute(f'select {key} from {table}'))
        current_app.logger.info(f'{table} has {len(ids)} records')
    except ProgrammingError:
        current_app.logger.warning(f'{table} doesn\'t exists')
        db.session.rollback()
        ids = {}
    return ids


def dedup_from_db(df, ids, key):
    if key == 'hash':
        df = df.apply(add_hash, axis=1)

    df = df[~df[key].isin(ids)]
    return df


def subset_df(multiplier, bucket_size, df):
    upper_limit = bucket_size * multiplier
    lower_limit = bucket_size * (multiplier - 1)
    return df[lower_limit:upper_limit]


def ingest_df(df, table):
    df.to_sql(table, db.engine, index=False, if_exists='append')
    return df


def bucket_df(df, batch_size):
    buckets = ceil(len(df) / batch_size)
    for multiplier in range(1, buckets + 1):
        yield subset_df(multiplier, batch_size, df)


def ingest_csv(table, csv, key='hash', batch_size=50):
    df = pandas.read_csv(csv).drop_duplicates()
    current_app.logger.info(f'{csv} has {len(df)} records')
    ids = get_ids(key, table)
    buckets = bucket_df(df, batch_size)

    with Pool(2) as p:
        current_app.logger.debug(f'Dedup starting at {datetime.now()}')
        dedupped_dfs = p.map(
            partial(dedup_from_db, ids=ids, key=key),
            buckets)
        current_app.logger.debug(f'Dedup ended at {datetime.now()}')

        current_app.logger.debug(f'Ingesting starting at {datetime.now()}')
        ingested_df = pandas.concat(p.map(
            partial(ingest_df, table=table),
            dedupped_dfs))
        current_app.logger.debug(f'Ingesting ended at {datetime.now()}')

    current_app.logger.info(f'Done inserting {len(ingested_df)} records into {table} from {csv}')
    return ingested_df
