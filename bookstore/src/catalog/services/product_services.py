from typing import Sequence

from bookstore.src.shared.errors import NotFoundError
from bookstore.src.catalog.entities import Product
from bookstore.src.shared.contracts.repository_interface import RepositoryInterface


class ProductServices:
    def __init__(self, repo: RepositoryInterface[Product]):
        self._repo = repo

    def get_product_list(self) -> Sequence[Product]:
        products = self._repo.filter_by()
        return products

    def get_product(self, product_id: int) -> Product:
        product = self._repo.get(product_id)

        if product is None:
            raise NotFoundError(f"Product #{product_id} not found")

        return product
