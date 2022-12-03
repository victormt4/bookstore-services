from typing import Sequence

from src.errors import NotFoundError
from src.catalog.entities import Product
from src.shared.contracts.repository import Repository


class ProductServices:

    def __init__(self, repo: Repository[Product]):
        self.__repo = repo

    def get_product_list(self) -> Sequence[Product]:
        return self.__repo.filter_by()

    def get_product(self, product_id: int) -> Product:
        product = self.__repo.get(product_id)

        if product is None:
            raise NotFoundError(f"Product #{product_id} not found")

        return product
