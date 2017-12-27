#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    api.main
    ~~~~~~~~~~~~~~
    api WSGI main entry point
"""
from insuratech.api import create_app
from insuratech.commands.ingest import ingest_cli

app = create_app()

app.cli.add_command(ingest_cli)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
