# -*- coding: utf-8 -*-
"""
    Insuratech test configuration
    ~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os
import pytest
from alembic.command import upgrade
from alembic.config import Config
from insuratech.api import create_app
from insuratech.api.base import _test_db
from insuratech.core import db as _db
from .. import settings


@pytest.yield_fixture(scope="session")
def app():
    app = create_app(settings)
    app_ctx = app.app_context()
    app_ctx.push()

    def teardown():
        app_ctx.pop()

    yield app

    teardown()


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope="session")
def db(app):
    def teardown():
        print('tearingdown db')
        _db.app = app
        print('reflecting db')
        _db.reflect()
        print('dropping all tables')
        _db.drop_all()
        print('done')

    def buildup_alembic():
        os.environ['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
        config = Config(app.config['ALEMBIC_CONFIG'])
        config.set_main_option('script_location', app.config['ALEMBIC_MIGRATIONS'])
        upgrade(config, 'head')

    print('building db')
    buildup_alembic()
    yield _db
    print('tearingdown db')
    teardown()


@pytest.yield_fixture(scope="function")
def session(db):
    def teardown():
        print('Tearing down session')
        transaction.rollback()
        connection.close()
        session.remove()
        print('Done')

    try:
        teardown()
    except Exception:
        pass

    print('Starting session')
    connection = db.engine.connect()
    transaction = connection.begin()
    session = db.create_scoped_session(options=dict(bind=connection, binds={}))
    db.session = session
    _test_db()

    yield session

    teardown()
