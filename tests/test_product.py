import json
import pytest

from models.product import Product


def test_create_product(test_app, monkeypatch):
    product_payload = {
        "name": "Ração para cachorro",
        "price": 50.0,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    }

    product_response = {
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
    assert response.json() == product_response

def test_get_product(test_app, monkeypatch):
    product_response = {
        "id": 1,
        "name": "Ração para gato",
        "price": 50,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    }

    def mock_get(db_session, name):
        return product_response

    monkeypatch.setattr(Product, "get_product", mock_get)

    product_name = "Ração para gato"

    response = test_app.get(f"/product/info?product_name={product_name}")
    assert response.status_code == 200
    assert response.json() == product_response

def test_list_products(test_app, monkeypatch):
    product_response = [
        {
            "id": 1,
            "name": "Ração para gato",
            "price": 50,
            "minimun": 10,
            "amount_per_package": 2,
            "max_availability": 50000
        },
        {
            "id": 2,
            "name": "Ração para coelho",
            "price": 30.0,
            "minimun": 2,
            "amount_per_package": 2,
            "max_availability": 70000
        }
    ]

    def mock_get_all(db_session):
        return product_response

    monkeypatch.setattr(Product, "get_all_products", mock_get_all)

    response = test_app.get("/product/list")
    assert response.status_code == 200
    assert response.json() == product_response

def test_delete_product(test_app, monkeypatch):
    product_data = {
        "id": 1,
        "name": "Ração para gato",
        "price": 50,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    },
    product_response = {
        "message": "Product deleted successfully"
    }

    def mock_get(db_session, id):
        return product_data

    monkeypatch.setattr(Product, "get_product_by_id", mock_get)

    def mock_delete(db_session, id):
        return product_data

    monkeypatch.setattr(Product, "delete_product", mock_delete)

    response = test_app.delete("/product/delete?product=1")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == product_response