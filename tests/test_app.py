# Tests for FastAPI application
from fastapi import FastAPI
from fastapi.testclient import TestClient

def test_root():
    # Test the root endpoint
    response = TestClient(FastAPI()).get("/")
    assert response.status_code == 200

def test_about():
    # Test the about page
    response = TestClient(FastAPI()).get("/about")
    assert response.status_code == 200

def test_contact():
    # Test the contact page
    response = TestClient(FastAPI()).get("/contact")
    assert response.status_code == 200

def test_login():
    # Test the login page
    response = TestClient(FastAPI()).get("/login")
    assert response.status_code == 200

def test_register():
    # Test the register page
    response = TestClient(FastAPI()).get("/register")
    assert response.status_code == 200

def test_routes():
    # Test all routes
    responses = []
    for route in FastAPI().routes:
        response = TestClient(FastAPI()).get(route)
        responses.append(response)
    assert len(responses) == FastAPI().routes.size