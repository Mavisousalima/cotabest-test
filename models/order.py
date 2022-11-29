from fastapi.exceptions import HTTPException
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Session, relationship

from database.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    shopping_cart_id = Column(Integer, ForeignKey("shopping_cart.id"))
    
    @staticmethod
    def create_order(shopping_cart_id, product_id: int, db: Session):
        order = Order(product_id=product_id, shopping_cart_id=shopping_cart_id)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    
    @staticmethod
    def get_orders(product_id: int, order_id: int, db: Session):
        order = db.query(Order).filter(Order.product_id == product_id,
                                       Order.id == order_id).all()
        return order