# -*- coding: utf-8 -*-
"""
    tests.insuratech.test_core
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests basic Insuratech functionality
"""
import pytest
from flask import url_for


@pytest.mark.functional
def test_ping(client, session):
    resp = client.get(url_for('ping'))
    assert resp.status_code == 200
