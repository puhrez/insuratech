# -*- coding: utf-8 -*-
"""
    commands.ingest
    ~~~~~~~~~~~~~~
    a command for csv ingestion
"""
import click
from flask.cli import AppGroup
from .helpers import ingest_csv

ingest_cli = AppGroup('ingest')


@ingest_cli.command('csv')
@click.option('--table', help='The table to ingest to')
@click.option('--csv', help="csv to ingest")
@click.option('--key', default='hash')
@click.option('--batch-size', default=50)
def csv_ingest_command(table, csv, key='hash', batch_size=50):
    ingested_df = ingest_csv(table, csv, key, batch_size)
    click.echo(f'{len(ingested_df)} records ingested')
