from fastapi.testclient import TestClient
from index import app

client = TestClient(app)

def test_get_one_pallet_success_status_code():
    response = client.get('/pallet_02')
    assert response.status_code == 200

def test_get_one_pallet_not_found_status_code():
    response = client.get('/pallet_01')
    assert response.status_code == 404

def test_get_one_pallet_response_type():
    response = client.get('/pallet_02')
    assert type(response.json()) is dict

def test_get_one_pallet_response():
    response = client.get('/pallet_02')
    assert response.json() == dict({
        "id": "pallet_02",
        "display_name": "string",
        "description": "string",
        "dimensions": {
            "height": 0,
            "depth": 0,
            "width": 0,
            "pallet_height": 0,
            "wheel_opening_width": 0
        }
    })