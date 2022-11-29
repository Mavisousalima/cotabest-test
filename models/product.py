from fastapi.exceptions import HTTPException
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Session, relationship

from database.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    price = Column(Float)
    minimun = Column(Integer)
    amount_per_package = Column(Integer)
    max_availability = Column(Integer)

    @staticmethod
    def get_product(name: str, db: Session):
        product = db.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
        if not product:
            raise HTTPException(status_code=400, detail="Product not found")
        return product

    @staticmethod
    def get_product_by_id(id: int, db: Session):
        product = db.query(Product).filter(Product.id == id).first()
        if not product:
            raise HTTPException(status_code=400, detail="Product not found")
        return product

    @staticmethod
    def get_all_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def create_product(name: str, price: int, minimun: int, amount_per_package: int, max_availability: int, db: Session):
        product = Product(
            name=name, 
            price=price, 
            minimun=minimun, 
            amount_per_package=amount_per_package, 
            max_availability=max_availability
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    
    @staticmethod
    def update_product(name: str, price: int, db: Session):
        product = Product.get_product(name, db)
        product.price = price
        db.commit()
        db.refresh(product)
        return product
    
    @staticmethod
    def delete_product(id: int, db: Session):
        product = Product.get_product_by_id(id, db)
        db.delete(product)
        db.commit()
        return product