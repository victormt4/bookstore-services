import pytest
from src.product.dto.product import Product
from src.product.services.product_services import get_product_list, get_product
from src.errors import NotFoundError


def test_get_product_list():
    product_list = get_product_list()

    assert len(product_list) == 10

    for product in product_list:
        assert type(product) == Product


def test_get_product():
    product_id = 1

    product = get_product(product_id)

    assert type(product) == Product
    assert product.id == product_id

    with pytest.raises(NotFoundError):
        get_product(100)
