from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# FIX: NEED MOCKING, STILL USING THE DB

def test_add_product_to_shopping_cart():
    response = client.post(
        "/product/add-to-cart",
        json={"id": 1},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product added to shopping cart successfully"
    }


def test_get_current_shopping_cart():
    response = client.get(
        "/product/shopping-cart",
    )
    assert response.status_code == 200
    assert response.json()[0] == {
        'id': 1,
        'shopping_cart_id': 1,
        'product_id': 1,
    }

def test_remove_product_from_shopping_cart():
    response = client.post(
        "/product/remove-from-cart",
        json={"id": 1},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product removed from shopping cart successfully"
    }


def test_delete_product(product_id: int):
    response = client.delete(
        f"/product/delete?product={product_id}",
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product Ração para gato 123 deleted successfully"
    }