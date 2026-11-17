from fastapi.testclient import TestClient

from app.main import app


def test_create_item():
    with TestClient(app) as client:
        r = client.post("/items", json={"name": "pen", "price_cents": 150})
        assert r.status_code == 200
        assert r.json()["name"] == "pen"
