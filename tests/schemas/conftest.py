import pytest
import requests


BASE_URL = "http://5.181.109.28:9090/api/v3"

@pytest.fixture(scope="function")
def create_pet():
    payload = {
        "id": 1,
        "name": "Buddy",
        "status": "available"
    }
    response = requests.post(url=f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    return response.json()

@pytest.fixture(scope="function")
def create_order():
    payload = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "status": "placed",
        "complete": True
    }
    response = requests.post(url=f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    return response.json()

@pytest.fixture(scope="function")
def create_booking():
    payload = {
    "bookingid": 1,
    "booking": {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
}
    response = requests.post(url=f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    return response.json()