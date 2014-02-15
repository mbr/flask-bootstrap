import pytest


@pytest.fixture
def app():
    from flask import Flask
    from flask_bootstrap import Bootstrap

    app = Flask(__name__)

    Bootstrap(app)

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    client.get('/')
