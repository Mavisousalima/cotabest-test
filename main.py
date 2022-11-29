from fastapi import FastAPI

from models.product import Product
from database.database import engine, Base

from routers.shopping_cart import shopping_cart_router
from routers.product import product_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(product_router)
app.include_router(shopping_cart_router)