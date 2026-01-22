from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "python_gc_objects" in response.text


def test_alerts():
    response = client.get("/")
    assert response.status_code == 200
