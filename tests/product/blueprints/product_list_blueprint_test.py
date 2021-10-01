import requests
import os


def test_products(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'products')
    response = requests.get(endpoint)
    assert response.status_code == 200

    request_data = response.json()

    assert type(request_data) == list
    assert len(request_data) == 10

    for product in request_data:
        assert type(product) == dict
        assert "id" in product
        assert "name" in product
        assert "author" in product
        assert "cover_picture" in product
        assert "description" in product
        assert "stock" in product
        assert "users_who_liked" in product
