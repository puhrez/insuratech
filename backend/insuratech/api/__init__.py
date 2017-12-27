# -*- coding: utf-8 -*-
"""

    insuratech.api
    ~~~~~~~~~~~~~~

    insuratech api application package
"""
from .. import factory
from .base import ping


def create_app(settings_override=None):
    app = factory.create_app(__name__, settings_override)
    app.logger.info(f'"{__name__}" created')
    if 'ping' not in app.view_functions:
        app.add_url_rule('/_ping', 'ping', ping)
    return app
