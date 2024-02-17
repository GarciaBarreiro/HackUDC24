import pytest
from flaskr.db import get_db

def test_register(client, app):
    # Test that viewing the page renders without template errors
    assert client.get('/auth/register').status_code == 200
    # Test that successful registration redirects to the login page
    response = client.post('/auth/register', data={'username': 'a', 'password': 'a'})
    assert 'http://localhost/auth/login' == response.headers['Location']

    # Test that the user was inserted into the database
    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
