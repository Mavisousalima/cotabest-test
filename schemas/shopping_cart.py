from pydantic import BaseModel

from models.product import Product


class ShoppingCart(BaseModel):
    id: int
    product: Product
    shopping_cart_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Ração para cachorro",
                "price": 50.0,
                "minimun": 10,
                "amount_per_package": 2,
                "max_availability": 50000
            }
        }