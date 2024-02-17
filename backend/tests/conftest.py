import pytest
from flaskr import start_app
from flaskr.db import get_db, init_db

@pytest.fixture
def app():
    app = start_app({'TESTING': True, 'DATABASE': 'flaskr.sqlite'})
    with app.app_context():
        init_db()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
