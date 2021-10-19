import pytest

from src.catalog.services.product_services import ProductServices
from tests.product_repo_mock import ProductRepoMock


@pytest.fixture()
def product_repo():
    return ProductRepoMock()


@pytest.fixture()
def product_services(product_repo):
    return ProductServices(product_repo)
