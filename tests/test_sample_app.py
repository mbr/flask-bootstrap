import pytest


@pytest.fixture
def app():
    import sys
    sys.path.append('.')

    from sample_application import create_app

    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    client.get('/')
