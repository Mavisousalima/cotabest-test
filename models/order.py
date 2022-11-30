from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session
from uuid import uuid4
from database.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    shopping_cart_id = Column(Integer, ForeignKey("shopping_cart.id"))
    
    @staticmethod
    def create_order(shopping_cart_id, product_id: int, db: Session):
        order = Order(id=str(uuid4()), product_id=product_id, shopping_cart_id=shopping_cart_id)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    
    @staticmethod
    def get_orders(product_id: int, order_id: int, db: Session):
        order = db.query(Order).filter(Order.product_id == product_id,
                                       Order.id == order_id).all()
        return order