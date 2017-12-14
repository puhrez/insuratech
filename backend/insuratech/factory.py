# -*- coding: utf-8 -*-
"""

   insuratech.factory
   ~~~~~~~~~~~~~~~~~~
"""
import sys
import logging
from flask import Flask
from .core import db


class ConfigException(Exception):
    pass


def create_app(package_name, settings_override=None):
    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('insuratech.settings')
    app.config.from_object(settings_override)

    if (app.debug or app.config['TESTING'] and app.config['ENVIRONMENT'] != 'docker') \
       and 'localhost' not in app.config['SQLALCHEMY_DATABASE_URI']:
        app.logger.warn('SQLALCHEMY_DATABASE_URI is not localhost')
        if app.config['TESTING']:
            raise ConfigException(
                'RUNNNING TESTS ON A REMOTE DATABASE IS TERRIBLY WASTEFUL')
    elif not app.debug:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in  %(pathname)s:%(lineno)d'))
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    db.init_app(app)

    return app
