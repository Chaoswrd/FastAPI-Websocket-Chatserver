from fastapi.testclient import TestClient
from fastapi import status
from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Not Found"}