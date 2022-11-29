from sqlalchemy.orm import Session

from models.product import Product


def create_product_view(name: str, price: int, minimun: int, amount_per_package: int, max_availability: int, db: Session):
    return Product.create_product(name, price, minimun, amount_per_package, max_availability, db)

def get_product_view(name: str, db: Session):
    return Product.get_product(name, db)

def delete_product_view(id: int, db: Session):
    return Product.delete_product(id, db)

def list_products_view(db: Session):
    return Product.get_all_products(db)