from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import List

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Root"}

@app.get("/about")
async def read_about():
    return {"message": "About"}

@app.get("/contact")
async def read_contact():
    return {"message": "Contact"}

@app.post("/login")
async def login(username: str, password: str):
    return {"message": f"Logged in as {username}"}

@app.post("/register")
async def register(username: str, password: str):
    return {"message": f"Registered {username}"}

test_client = TestClient(app)

def test_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Root"}

def test_about():
    response = test_client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "About"}

def test_contact():
    response = test_client.get("/contact")
    assert response.status_code == 200
    assert response.json() == {"message": "Contact"}

def test_login():
    response = test_client.post("/login", json={"username": "user1", "password": "password1"})
    assert response.status_code == 200
    assert response.json() == {"message": f"Logged in as user1"}

def test_register():
    response = test_client.post("/register", json={"username": "user2", "password": "password2"})
    assert response.status_code == 200
    assert response.json() == {"message": f"Registered user2"}