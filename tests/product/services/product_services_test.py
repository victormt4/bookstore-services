import pytest
from src.product.dto.product import Product
from src.product.services.product_services import ProductServices
from src.errors import NotFoundError


@pytest.fixture()
def product_services():
    yield ProductServices()


def test_get_product_list(product_services):
    product_list = product_services.get_product_list()

    assert len(product_list) == 10

    for product in product_list:
        assert type(product) == Product


def test_get_product(product_services):
    product_id = 1

    product = product_services.get_product(product_id)

    assert type(product) == Product
    assert product.id == product_id

    with pytest.raises(NotFoundError):
        product_services.get_product(100)
