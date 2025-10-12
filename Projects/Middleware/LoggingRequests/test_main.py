
from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

def test_hello_world():
    name = "Arjun"
    response = client.get(f"/api/say_hello/{name}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": f"Hello: {name}"}

def test_welcome():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Welcome to Logging Middleware Practice"}
