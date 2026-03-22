from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

products = [
    Product(id=1, name="Mobile", price=500.99),
    Product(id=2, name="Smart Watch", price=200.99),
    Product(id=3, name="Laptop", price=999.9),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")
def get_products_by_id(id: int):
    return products[id-1]