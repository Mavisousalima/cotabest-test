import json
import pytest

from models.shopping_cart import ShoppingCart
from models.product import Product


def test_add_product_to_shopping_cart(test_app, monkeypatch):
    cart_payload = {
        "id": 1,
        "amount": 10
    }

    def mock_post(db_session, shopping_cart_id, id, amount):
        return cart_payload

    monkeypatch.setattr(ShoppingCart, "add_product_to_shopping_cart", mock_post)

    response = test_app.post("/shopping-cart/add-to-cart?shopping_cart_id=1", data=json.dumps(cart_payload))
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product added to shopping cart successfully"
    }

"""def test_product_minimun_quantity(test_app, monkeypatch):
    product_payload = {
        "id": 1,
        "name": "Ração para cachorro",
        "price": 50.0,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    }

    def mock_post(db_session, name, price, minimun, amount_per_package, max_availability):
        return product_payload

    monkeypatch.setattr(Product, "create_product", mock_post)

    response = test_app.post("/product/create", data=json.dumps(product_payload))

    assert response.status_code == 201

    cart_payload = {
        "id": 1,
        "amount": 2
    }

    def mock_post(db_session, shopping_cart_id, id, amount):
        return cart_payload

    monkeypatch.setattr(ShoppingCart, "add_product_to_shopping_cart", mock_post)

    response = test_app.post("/shopping-cart/add-to-cart?shopping_cart_id=1", data=json.dumps(cart_payload))
    assert response.status_code == 400
    assert response.json() == {"message": "Minimum quantity for this product: 10"}"""

def test_get_current_shopping_cart(test_app, monkeypatch):
    cart_response = {
        "product_id": 1,
        "id": 1,
        "shopping_cart_id": 1
    }

    def mock_get(db_session, shopping_cart_id):
        return cart_response

    monkeypatch.setattr(ShoppingCart, "get_current_shopping_cart", mock_get)

    response = test_app.get("/shopping-cart/shopping-cart?shopping_cart_id=1")
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'shopping_cart_id': 1,
        'product_id': 1,
    }