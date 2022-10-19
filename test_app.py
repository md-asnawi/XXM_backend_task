from fastapi.testclient import TestClient
from index import app

client = TestClient(app)

def test_get_all_pallets():
    response = client.get('/')
    assert response.status_code == 200