# -*- coding: utf-8 -*-
"""
    tests.commands.ingest
    ~~~~~~~~~~~~~~
    tests for ingest commands
"""
import pytest
import pandas
from sqlalchemy.exc import ProgrammingError
from insuratech.commands.ingest import ingest_csv


@pytest.mark.integration
def test_csv_ingest(session):
    csv = 'tests/data/data-small.csv'
    table = 'test_table'

    # test can create table
    with pytest.raises(ProgrammingError):
        session.execute(f'select count(*) from {table}').first()['count']
    session.rollback()

    # test ingestion
    ingest_csv(table, csv)
    df = pandas.read_csv(csv)
    assert session.execute(f'select count(*) from {table}').first()['count'] == len(df)

    # test idempotence
    ingest_csv(table, csv)
    assert session.execute(f'select count(*) from {table}').first()['count'] == len(df)
