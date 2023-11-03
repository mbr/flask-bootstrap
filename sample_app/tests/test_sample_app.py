import pytest


@pytest.fixture
def app():
    import sys
    sys.path.append('.')

    from sample_app import create_app

    app = create_app()
    app.debug = True
    app.testing = True

    # manually add flask-debug
    from flask_debug import Debug
    Debug(app)

    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
