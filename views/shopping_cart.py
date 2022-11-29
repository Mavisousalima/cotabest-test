from sqlalchemy.orm import Session

from models.shopping_cart import ShoppingCart


def add_product_to_shopping_cart_view(shopping_cart_id: int, product_id: int, amount: int, db: Session):
    return ShoppingCart.add_product_to_shopping_cart(shopping_cart_id, product_id, amount, db)

def remove_product_from_shopping_cart_view(shopping_cart_id: int, product_id: int, db: Session):
    return ShoppingCart.remove_product_from_shopping_cart(shopping_cart_id, product_id, db)

def get_current_shopping_cart_view(shopping_cart_id: int, db: Session):
    return ShoppingCart.get_current_shopping_cart(shopping_cart_id, db)

def update_product_from_shopping_cart_view(shopping_cart_id: int, amount: int, db: Session):
    return ShoppingCart.update_product_from_shopping_cart(shopping_cart_id=shopping_cart_id, amount=amount, db=db)