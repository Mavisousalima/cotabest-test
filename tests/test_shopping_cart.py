import json
import pytest

from models.shopping_cart import ShoppingCart


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

"""def test_remove_product_from_shopping_cart(test_app, monkeypatch):
    response = test_app.post(
        "/product/remove-from-cart",
        json={"id": 1},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product removed from shopping cart successfully"
    }"""