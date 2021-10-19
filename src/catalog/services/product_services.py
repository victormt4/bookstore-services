from typing import List

from src.errors import NotFoundError
from src.catalog.entities import Product
from src.shared.contracts.repository import Repository


class ProductServices:

    def __init__(self, repo: Repository[Product]):
        self.__repo = repo

    def get_product_list(self) -> List[Product]:
        """
        Return a list of Product
        :rtype: List[Product]
        """
        return self.__repo.get_all()

    def get_product(self, product_id: int) -> Product:
        """
        Get a product by id
        :rtype: Product
        :raises NotFoundError
        """
        product = self.__repo.get(product_id)

        if product is None:
            raise NotFoundError(f"Product #{product_id} not found")

        return product
