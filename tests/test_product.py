from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# FIX: NEED MOCKING, STILL USING THE DB

def test_create_product():
    response = client.post(
        "/product/create",
        json={
            "name": "Ração para gato 123",
            "price": 50,
            "minimun": 10,
            "amount_per_package": 2,
            "max_availability": 50000
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Product Ração para gato 123 created successfully"
    }

def test_get_product():
    response = client.post("/product/info", json={"name": "Ração para gato"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Ração para gato 123",
        "price": 50,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    }


def test_list_products():
    response = client.get("/product/list")
    print(response.json())
    assert response.status_code == 200
    assert response.json()[0] == {
        "id": 1,
        "name": "Ração para gato 123",
        "price": 50,
        "minimun": 10,
        "amount_per_package": 2,
        "max_availability": 50000
    }


