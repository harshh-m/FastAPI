from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

products = [
    Product(id=1, name="Mobile", price=500.99),
    Product(id=2, name="Smart Watch", price=200.99),
    Product(id=8, name="Laptop", price=999.9),
]

@app.get("/product")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"

@app.post("/create-product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/update-product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return"Product updated successfully"
    return " No Product found"

@app.delete("/delete-product/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully"
    return "No Product found"