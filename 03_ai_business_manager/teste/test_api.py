from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analyze_endpoint_without_ai():
    response = client.post("/analyze", json={
        "records": [{"product": "Desk", "category": "Office", "quantity": 2, "unit_price": 50}],
        "use_ai": False,
    })
    assert response.status_code == 200
    assert response.json()["metrics"]["total_revenue"] == 100
    assert response.json()["ai"]["mode"] == "not_requested"
