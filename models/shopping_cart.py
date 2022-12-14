from fastapi.exceptions import HTTPException
from sqlalchemy import Column,Integer
from sqlalchemy.orm import Session, relationship

from database.database import Base
from .product import Product
from .order import Order
from schemas.shopping_cart import ShoppingCart


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    orders = relationship("Order", backref="shopping_cart")

    @staticmethod
    def get_shopping_cart(db: Session, id: int):
        shopping_cart = db.query(ShoppingCart).filter(
            ShoppingCart.id == id).first()
        return shopping_cart

    @staticmethod
    def get_current_shopping_cart(shopping_cart_id: int, db: Session):
        shopping_cart = db.query(ShoppingCart).filter(
            ShoppingCart.id == shopping_cart_id).first()
        if not shopping_cart:
            raise HTTPException(status_code=404, detail="Shopping cart not found")

        order = db.query(Order).filter(Order.shopping_cart_id == shopping_cart_id).all()
        
        items = []
        for i in range(len(order)):
            items.append(db.query(Product).filter(Product.id == order[i].product_id).first())

        shopping_cart_data = {
            "order": shopping_cart.orders[0].id,
            "items": items
        }

        return shopping_cart_data

    @staticmethod
    def create_shopping_cart(amount: int, db: Session):
        shopping_cart = ShoppingCart(amount=amount)
        db.add(shopping_cart)
        db.commit()
        db.refresh(shopping_cart)
        return shopping_cart

    @staticmethod
    def add_product_to_shopping_cart(shopping_cart_id: int, product_id: int, amount: int, db: Session):
        shopping_cart = db.query(ShoppingCart).filter(ShoppingCart.id == shopping_cart_id).first()
        if not shopping_cart:
            shopping_cart = ShoppingCart.create_shopping_cart(amount, db)

        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.minimun > amount:
            raise HTTPException(status_code=400, detail=f"Minimum quantity for this product: {product.minimun}")

        if product.max_availability < amount:
            raise HTTPException(status_code=400, detail=f"Desired quantity exceeds available quantity. MAX: {product.max_availability}")

        order = Order.create_order(shopping_cart.id, product.id, db)
        shopping_cart.orders.append(order)
        db.commit()
        db.refresh(shopping_cart)
        return shopping_cart

    @staticmethod
    def remove_product_from_shopping_cart(shopping_cart_id: int, product_id: int,
                                          db: Session):
        shopping_cart = db.query(ShoppingCart).filter(
            ShoppingCart.id == shopping_cart_id).first()
        if not shopping_cart:
            raise HTTPException(status_code=404, detail="Shopping cart not found")
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        order = Order.get_orders(product_id, shopping_cart.id, db)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        for item in order:
            db.delete(item)
        db.commit()
        db.refresh(shopping_cart)
        return shopping_cart

    @staticmethod
    def update_product_from_shopping_cart(shopping_cart_id: int, amount: int, db: Session):
        shopping_cart = db.query(ShoppingCart).filter(
            ShoppingCart.id == shopping_cart_id).first()
        if not shopping_cart:
            raise HTTPException(status_code=400, detail="Cart not found")
        shopping_cart.amount = amount
        db.add(shopping_cart)
        db.commit()
        db.refresh(shopping_cart)
        return shopping_cart