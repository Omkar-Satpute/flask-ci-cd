import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app
import pytest # type: ignore

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, CI/CD with Kubernetes!" in response.data

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}