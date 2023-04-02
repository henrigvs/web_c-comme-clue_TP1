import pytest
from flask import Flask

from src.users.api.controller.UserController import userBP


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(userBP, url_prefix="/users")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_addUser(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    response = client.post("/users/addUser", json=data)
    assert response.status_code == 201


def test_addUser_existing_email(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    client.post("/users/addUser", json=data)

    data = {
        'firstName': 'Grace',
        'lastName': 'Hopper',
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    response = client.post("/users/addUser", json=data)
    assert response.status_code == 400


def test_getAllUsers(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    client.post("/users/addUser", json=data)

    data = {
        'firstName': 'Allan',
        'lastName': 'turing',
        'email': 'allan.turing@example.com',
        'password': 'password123'
    }
    client.post("/users/addUser", json=data)

    response = client.get("/users/allUsers")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_getUserById(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    response = client.post("/users/addUser", json=data)
    jsonResponse = response.json
    userId = jsonResponse['userId']

    response = client.get(f"/users/{userId}")
    assert response.status_code == 200
    assert jsonResponse['firstName'] == "Ada"
    assert jsonResponse['email'] == "ada.lovelace@example.com"


def test_editUser(client):
    # Given
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123',
        'isConnected': True
    }
    response = client.post("/users/addUser", json=data)
    jsonResponse = response.json
    userId = jsonResponse['userId']

    # When
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'newPassword',
        'isConnected': True
    }
    response = client.put(f"/users/{userId}", json=data)
    jsonResponse = response.json

    # Then
    assert response.status_code == 200
    assert jsonResponse['password'] == "newPassword"


def test_connectAnUserByEmailAndPassword(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123',
        'isConnected': False
    }
    client.post("/users/addUser", json=data)

    data = {
        'email': 'ada.lovelace@example.com',
        'password': 'password123'
    }
    response = client.put('/users/login', json=data)
    jsonResponse = response.json
    assert response.status_code == 200
    assert jsonResponse['isConnected'] == True


def test_disconnectAnUserByUserId(client):
    data = {
        'firstName': 'Ada',
        'lastName': 'Lovelace',
        'email': 'ada.lovelace@example.com',
        'password': 'password123',
        'isConnected': True
    }
    response = client.post("/users/addUser", json=data)
    jsonResponse = response.json
    userId = jsonResponse['userId']

    data = {
        'userId': f"{userId}"
    }
    response = client.put('/users/logout', json=data)
    assert response.status_code == 200
    assert response.json['isConnected'] == False
