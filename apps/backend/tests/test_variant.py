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


def test_variant_scoring():
    client = TestClient(app)
    client.post('/api/v1/auth/register', json={'email': 'a@b.com', 'password': 'pw'})
    login = client.post('/api/v1/auth/login', data={'username': 'a@b.com', 'password': 'pw'})
    token = login.json()['access_token']
    st = client.post('/api/v1/sitetwins/', json={'name': 'Test'}, headers={'Authorization': f'Bearer {token}'})
    st_id = st.json()['id']
    variant = client.post('/api/v1/variants/', json={'site_twin_id': st_id, 'name': 'Var1'})
    variant_id = variant.json()['id']
    score = client.post(f'/api/v1/variants/{variant_id}/score')
    assert score.json()['score_primary'] == len('Var1')
