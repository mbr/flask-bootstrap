import re

from flask import Flask
from flask_bootstrap import (Bootstrap, get_bootstrap_version,
                             BOOTSTRAP_VERSION_RE, BOOTSTRAP_VERSION)
import requests

import pytest


@pytest.fixture
def app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_bootstrap_version_regular_expression():
    assert get_bootstrap_version('3.3.7.1') == '3.3.7'
    assert get_bootstrap_version('3.3.7.2.dev1') == '3.3.7'
    assert get_bootstrap_version('3.7.11.12') == '3.7.11'
    assert get_bootstrap_version('4.0.0-beta.0.dev1') == '4.0.0-beta'
    assert get_bootstrap_version('4.0.0-beta.1') == '4.0.0-beta'


def test_bootstrap_version_matches(app, client):
    bootstrap_vre = re.compile(r'Bootstrap v' + BOOTSTRAP_VERSION_RE.pattern)

    # find local version
    local_version = bootstrap_vre.search(
        str(client.get('/static/bootstrap/css/bootstrap.css').data)
    ).group(1)

    # find cdn version
    cdn = app.extensions['bootstrap']['cdns']['bootstrap']
    with app.app_context():
        cdn_url = 'https:' + cdn.get_resource_url('css/bootstrap.css')
    cdn_version = bootstrap_vre.search(requests.get(cdn_url).text).group(1)

    # get package version

    assert local_version == BOOTSTRAP_VERSION
    assert cdn_version == BOOTSTRAP_VERSION
