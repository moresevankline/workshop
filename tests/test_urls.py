import pytest
import requests
import uuid
import secrets

BASE_URL = "https://workshop-uw8o.onrender.com"


def test_obtain_token():
    response = requests.post(f"{BASE_URL}/user/token/", json={
        "username": "franz",
        "password": "franz123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access" in data
    assert "refresh" in data


def test_user_registration():
    # Generate a random username and password
    random_username = f"user_{uuid.uuid4().hex[:8]}"
    random_password = secrets.token_urlsafe(12)

    response = requests.post(f"{BASE_URL}/user/registration/", json={
        "username": random_username,
        "password": random_password,
        "country": "Philippines"
    })

    # 201 if registration successful
    assert response.status_code == 201


def test_user_registration_exists():

    response = requests.post(f"{BASE_URL}/user/registration/", json={
        "username": "franz",
        "password": "franz123",
        "country": "Philippines"
    })

    # 201 if registration successful
    assert response.status_code == 400

def test_user_registration_exists():

    response = requests.post(f"{BASE_URL}/user/registration/", json={
        "username": "franz",
        "password": "franz123",
        "country": "Philippines"
    })

    # 201 if registration successful
    assert response.status_code == 400
    

def test_obtain_token_wrong_credentials():
    response = requests.post(f"{BASE_URL}/user/token/", json={
        "username": "franz",
        "password": "franz1234"
    })
    assert response.status_code == 401

