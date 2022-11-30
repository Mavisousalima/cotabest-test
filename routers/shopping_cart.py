from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.product import ProductID
from views.shopping_cart import (add_product_to_shopping_cart_view,
                    get_current_shopping_cart_view,
                    remove_product_from_shopping_cart_view,
                    update_product_from_shopping_cart_view)
from database.utils import get_db

shopping_cart_router = APIRouter(
    prefix="/shopping-cart",
    tags=["shopping cart"],
    responses={404: {
        "description": "Not found"
    }},
)


@shopping_cart_router.post("/add-to-cart",
             status_code=status.HTTP_200_OK,
             summary="Add product to shopping cart",
             responses={
                 200: {
                     "description":
                     "Product added to shopping cart successfully",
                     "content": {
                         "application/json": {
                             "example": {
                                 "message":
                                 "Product added to shopping cart successfully"
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
                 }
             })
def add_product_to_shopping_cart(shopping_cart_id: int, product: ProductID, db: Session = Depends(get_db)):
    add_product_to_shopping_cart_view(shopping_cart_id, product.id, product.amount, db)
    return {"message": "Product added to shopping cart successfully"}

@shopping_cart_router.post(
    "/remove-from-cart",
    status_code=status.HTTP_200_OK,
    summary="Remove product from shopping cart",
    responses={
        200: {
            "description": "Product removed from shopping cart successfully",
            "content": {
                "application/json": {
                    "example": {
                        "message":
                        "Product removed from shopping cart successfully"
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
        }
    })
def remove_product_from_shopping_cart(shopping_cart_id: int, product: int, db: Session = Depends(get_db)):
    remove_product_from_shopping_cart_view(shopping_cart_id, product, db)
    return {"message": "Product removed from shopping cart successfully"}


@shopping_cart_router.get("/shopping-cart",
            status_code=status.HTTP_200_OK,
            summary="Open shopping cart information",
            responses={
                200: {
                    "description": "Shopping cart information",
                    "content": {
                        "application/json": {
                            "example": [{
                                "id": 1,
                                "shopping_cart_id": 1,
                                "product_id": 1
                            }]
                        }
                    }
                },
            })
def get_current_shopping_cart(shopping_cart_id: int, db: Session = Depends(get_db)):
    shopping_cart = get_current_shopping_cart_view(shopping_cart_id, db)
    return shopping_cart

@shopping_cart_router.put("/update-cart", status_code=status.HTTP_200_OK)
def update_shopping_cart(shopping_cart_id: int, product: ProductID, db: Session = Depends(get_db)):
    shopping_cart = update_product_from_shopping_cart_view(shopping_cart_id, product.amount, db)

    return shopping_cart
