import time 
from fastapi.testclient import TestClient
from app.main import app
from app import services

client = TestClient(app)

services.cache["USD"] = {"time": time.time(), "rates": {"USD": 1, "NGN": 1500, "EUR": 0.9}}

def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_conversion_logic():
    rate, result = services.convert(10, "USD", "NGN")
    assert rate == 1500
    assert result == 15000

def test_convert_endpoint():
    response = client.get("/convert?amount=10&from_currency=USD&to_currency=EUR")
    assert response.status_code == 200
    assert response.json()["result"] == 9.0


def test_bad_amount():
    response = client.get("/convert?amount=-5&from_currency=USD&to_currency=EUR")
    assert response.status_code == 400

def test_invalid_currency():
    response = client.get("/convert?amount=10&from_currency=USD&to_currency=XYZ")
    assert response.status_code == 404