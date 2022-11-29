from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.product import ProductCreate
from views.product import (create_product_view, get_product_view, list_products_view, delete_product_view)
from database.utils import get_db

product_router = APIRouter(
    prefix="/product",
    tags=["products"],
    responses={404: {
        "description": "Not found"
    }},
)


@product_router.post("/create",
             status_code=status.HTTP_201_CREATED,
             summary="Create a new product",
             responses={
                 201: {
                     "description": "Product created successfully",
                     "content": {
                         "application/json": {
                             "example": {
                                 "message":
                                 "Product {name} created successfully"
                             }
                         }
                     }
                 },
                 400: {
                     "description": "Product already exists",
                     "content": {
                         "application/json": {
                             "example": {
                                 "detail": "Product already exists"
                             }
                         }
                     }
                 }
             })
             
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = create_product_view(product.name, product.price, product.minimun, product.amount_per_package, product.max_availability, db)
    return product

@product_router.get("/info",
             status_code=status.HTTP_200_OK,
             summary="Get product info",
             responses={
                 200: {
                     "description": "Product info",
                     "content": {
                         "application/json": {
                             "example": {
                                 "id": 1,
                                 "name": "Ração para cachorro",
                                 "price": 50.0,
                                 "minimun": 10,
                                 "amount_per_package": 2,
                                 "max_availability": 50000
                             }
                         }
                     }
                 },
                 404: {
                     "description": "Not found",
                     "content": {
                         "application/json": {
                             "example": {
                                 "detail": "Product not found"
                             }
                         }
                     }
                 },
             })
def get_product(product_name: str, db: Session = Depends(get_db)):
    product = get_product_view(product_name, db)
    return product

@product_router.delete("/delete",
               status_code=status.HTTP_200_OK,
               summary="Delete a product",
               responses={
                   200: {
                       "description": "Product deleted successfully",
                       "content": {
                           "application/json": {
                               "example": {
                                   "message":
                                   "Product {name} deleted successfully"
                               }
                           }
                       }
                   },
                   404: {
                       "description": "Not found",
                       "content": {
                           "application/json": {
                               "example": {
                                   "detail": "Product not found"
                               }
                           }
                       }
                   },
               })
def delete_product(product: int, db: Session = Depends(get_db)):
    product = delete_product_view(product, db)
    return {"message": "Product deleted successfully"}


@product_router.get("/list",
            status_code=status.HTTP_200_OK,
            summary="List all products",
            responses={
                200: {
                    "description": "List of products",
                    "content": {
                        "application/json": {
                            "example": [{
                                "id": 1,
                                "name": "Ração para cachorro",
                                "price": 50.0,
                                "minimun": 10,
                                "amount_per_package": 2,
                                "max_availability": 50000
                            }, {
                                "id": 2,
                                "name": "Ração para coelho",
                                "price": 30.0,
                                "minimun": 2,
                                "amount-per-package": 2,
                                "max-availability": 70000
                            }]
                        }
                    }
                },
            })
def list_products(db: Session = Depends(get_db)):
    products = list_products_view(db)
    return products