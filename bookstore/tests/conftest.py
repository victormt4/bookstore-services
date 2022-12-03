import pytest

from bookstore.src.catalog.services.product_services import ProductServices
from bookstore.tests.repo_mock import ProductRepoMock, CouponRepoMock


@pytest.fixture()
def product_repo():
    return ProductRepoMock()


@pytest.fixture()
def coupon_repo():
    return CouponRepoMock()


@pytest.fixture()
def product_services(product_repo):
    return ProductServices(product_repo)
