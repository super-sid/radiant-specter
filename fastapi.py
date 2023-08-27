from fastapi import FastAPI, APIRouter, Depends
from fastapi.templating import Template
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Define a router for the application
router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@router.get("/about")
def read_about():
    return {"message": "This is the about page"}

@router.post("/contact")
def handle_contact(name: str, email: str):
    return {"message": f"Thank you for your contact form submission {name} ({email})"}

@router.get("/login")
def read_login():
    return {"message": "Log in to access the rest of the app"}

@router.post("/register")
def handle_register(name: str, email: str):
    return {"message": f"Registration successful {name} ({email})"}

# Define a template for the home page
home_template = Template("home", "templates/home.html")

# Define a template for the about page
about_template = Template("about", "templates/about.html")

# Define a template for the contact page
contact_template = Template("contact", "templates/contact.html")

# Define a template for the login page
login_template = Template("login", "templates/login.html")

# Define a template for the register page
register_template = Template("register", "templates/register.html")

@app.get("/home")
def home():
    return home_template.render(title="Home")

@app.get("/about")
def about():
    return about_template.render(title="About")

@app.get("/contact")
def contact():
    return contact_template.render(title="Contact")

@app.post("/login")
def login():
    return JSONResponse(content={"message": "Logged in successfully"})

@app.post("/register")
def register():
    return JSONResponse(content={"message": "Registration successful"})

# Define a route for the application
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!", "version": app.version}