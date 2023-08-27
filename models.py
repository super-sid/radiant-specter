from fastapi import FastAPI, Model
from typing import List

class User(Model):
    id = int
    name = str
    email = str

class Product(Model):
    id = int
    name = str
    price = float
    category = str

class Order(Model):
    id = int
    user_id = int
    products = List[Product]