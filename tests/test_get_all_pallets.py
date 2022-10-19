from fastapi.testclient import TestClient
from index import app

client = TestClient(app)

def test_get_all_pallets_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_get_all_pallets_response_type():
    response = client.get('/')
    assert type(response.json()) is list