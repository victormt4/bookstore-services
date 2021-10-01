from src.product.dto.product import Product
from src.product.services.product_services import get_product_list


def test_get_product_list():
    product_list = get_product_list()

    assert len(product_list) == 10

    for product in product_list:
        assert type(product) == Product
