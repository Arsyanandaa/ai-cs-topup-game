from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_ask_mobile_legends():
    response = client.post("/ask", json={"message": "cara top up mobile legends"})
    assert response.status_code == 200
    assert "Mobile Legends" in response.json()["answer"]


def test_ask_free_fire():
    response = client.post("/ask", json={"message": "top up free fire"})
    assert response.status_code == 200
    assert "Free Fire" in response.json()["answer"]


def test_ask_unknown():
    response = client.post("/ask", json={"message": "pertanyaan random"})
    assert response.status_code == 200
    assert "Maaf" in response.json()["answer"]