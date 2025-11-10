import pytest

def test_create_user(client):
    payload = {"username": "alice", "email": "alice@example.com", "password": "Secret123!"}
    r = client.post("/users", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data

def test_uniqueness_username_email(client):
    payload = {"username": "bob", "email": "bob@example.com", "password": "Secret123!"}
    r1 = client.post("/users", json=payload)
    assert r1.status_code == 201
    # duplicate username
    r2 = client.post("/users", json={"username": "bob", "email": "bob2@example.com", "password": "Secret123!"})
    assert r2.status_code == 400
    # duplicate email
    r3 = client.post("/users", json={"username": "bob2", "email": "bob@example.com", "password": "Secret123!"})
    assert r3.status_code == 400

def test_invalid_email_rejected(client):
    r = client.post("/users", json={"username": "c", "email": "bademail", "password": "Secret123!"})
    assert r.status_code in (400, 422)  # FastAPI returns 422 for request body validation failures