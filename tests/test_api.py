from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_kpis_and_forecast():
    assert client.get("/analytics/kpis").json()["orders"] > 0
    assert len(client.get("/forecasts/demand?periods=2").json()) == 2
