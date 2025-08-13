import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app
from app.db.base import Base
from app.db.session import engine
import pytest


@pytest.fixture(autouse=True)
def _setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_register_and_login():
    client = TestClient(app)
    resp = client.post('/api/v1/auth/register', json={'email': 'user@example.com', 'password': 'secret'})
    assert resp.status_code == 200
    login = client.post('/api/v1/auth/login', data={'username': 'user@example.com', 'password': 'secret'})
    assert login.status_code == 200
    token = login.json()['access_token']
    me = client.get('/api/v1/auth/users/me', headers={'Authorization': f'Bearer {token}'})
    assert me.status_code == 200
    assert me.json()['email'] == 'user@example.com'
