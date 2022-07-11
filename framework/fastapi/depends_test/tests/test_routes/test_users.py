import json


def test_create_user(client):
    data = {
        "username": "testusername",
        "email": "test@example.com",
        "password": "123456",
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["is_active"] is True
