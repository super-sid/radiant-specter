from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.templating import Template

def test_schema():
    # Test that the schema is valid
    data = {"name": "John", "age": 30}
    response = FastAPI().get("/users/1")
    assert response.status_code == 200
    assert response.content == JSONResponse(data, media_type="application/json")