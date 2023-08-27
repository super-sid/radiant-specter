from fastapi import FastAPI, Route, HTTPException
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get("/")
async def read_root():
    return {"message": "Welcome to the root page!"}

@app.get("/about")
async def read_about():
    return {"message": "Learn more about FastAPI!"}

@app.post("/contact")
async def create_contact(name: str, email: str):
    return {"message": f"Thank you for your contact request {name} ({email})"}

@app.get("/login")
async def read_login():
    return {"message": "Log in to access the rest of the application"}

@app.post("/register")
async def create_account(name: str, email: str):
    return {"message": f"Account created {name} ({email})"}

@app.get("/home")
async def read_home():
    return {"message": "You are here"}

@app.post("/home")
async def update_home(name: str, email: str):
    return {"message": f"Your homepage has been updated {name} ({email})"}