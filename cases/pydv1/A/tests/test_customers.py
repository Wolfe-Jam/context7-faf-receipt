from fastapi.testclient import TestClient

from app.main import app


def test_get_customer():
    r = TestClient(app).get("/customers/1")
    assert r.status_code == 200
    assert r.json()["name"] == "Ada"
