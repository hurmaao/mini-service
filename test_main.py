from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "cpu" in response.json()

def test_alerts():
    response = client.get("/alerts")
    assert response.status_code == 200
    assert len(response.json()) > 0

