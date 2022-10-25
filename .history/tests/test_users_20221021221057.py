from email import message
import email
from urllib import response
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    print(response.json().get("status"))
    assert response.json().get("status") == 'mainkek.py'
    assert response.status_code == 200


def test_create_user():
    response = client.get(
        '/users/', json={'email': 'p6pp@gmail.com', 'password': 'asdf'})
    print(response.json())
    assert response.json().get('email') == 'p6pp@gmail.com'
    assert response.status_code == 201
