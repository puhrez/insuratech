# -*- coding: utf-8 -*-
"""
    insuratech.api.base
    ~~~~~~~~~~~~~~~~~~

    Insuratech API Base utilities
"""
from sqlalchemy.exc import OperationalError
from werkzeug import exceptions as e
from ..core import db  # noqa


class DBUnavailable(e.ServiceUnavailable):
    pass


def _test_db():
    try:
        db.session.execute('select * from alembic_version')
        return True
    except OperationalError:
        db.session.rollback()
        return False


def ping():
    if _test_db():
        return 'OK'
    else:
        raise DBUnavailable
