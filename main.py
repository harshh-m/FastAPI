from fastapi import FastAPI,Depends
from models import Product
from database import session , engine
import database_models
from sqlalchemy.orm import Session

database_models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

products = [
    Product(id=1, name="Mobile", price=500.99),
    Product(id=2, name="Smart Watch", price=200.99),
    Product(id=8, name="Laptop", price=999.9),
]
def init__db():
    db = session()
    count= db.query(database_models.Product).count()
    if count ==0:
        for product in products:
            db_add = database_models.Product(**product.model_dump())
            db.add(db_add)
        db.commit()

init__db()


@app.get("/product")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()



@app.get("/product/{id}")
def get_product_by_id(id: int,db: Session = Depends(get_db)):
        db_product= db.query(database_models.Product).filter(database_models.Product.id == id).first()
        if db_product:
            return db_product
        return "Product not found"

@app.post("/create-product")
def add_product(product: Product,db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    return product

@app.put("/update-product/{id}")
def update_product(id: int, product: Product,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db.commit()
        return"Product updated successfully"
    else:
        return "Product not found"   

@app.delete("/delete-product/{id}")
def delete_product(id:int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully"
    else:
        return "Product not found"
        
   