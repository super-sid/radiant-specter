from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from typing import List

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.post("/users")
async def create_user(user: dict):
    return JSONResponse(status_code=201, content={"message": "User created successfully"})

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return JSONResponse(content={"message": "User details for id {user_id}"})

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: dict):
    return JSONResponse(status_code=200, content={"message": "User updated successfully"})

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return JSONResponse(status_code=204, content={"message": "User deleted successfully"})

@app.get("/items")
async def read_items():
    return JSONResponse(content={"message": "Items list"})

@app.post("/items")
async def create_item(item: dict):
    return JSONResponse(status_code=201, content={"message": "Item created successfully"})

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return JSONResponse(content={"message": "Item details for id {item_id}"})

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return JSONResponse(status_code=200, content={"message": "Item updated successfully"})

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return JSONResponse(status_code=204, content={"message": "Item deleted successfully"})