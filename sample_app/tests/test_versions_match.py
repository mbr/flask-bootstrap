import re

from flask import Flask
from flask_bootstrap import Bootstrap
import flask_bootstrap
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


@pytest.fixture
def bsv():
    bootstrap_version = re.search(r'(\d+\.\d+\.\d+)',
                                  str(flask_bootstrap.__version__)).group(1)
    return bootstrap_version


def test_bootstrap_version_matches(app, client, bsv):
    bootstrap_vre = re.compile(r'Bootstrap v(\d+\.\d+\.\d+).*')

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

    assert local_version == bsv
    assert cdn_version == bsv
