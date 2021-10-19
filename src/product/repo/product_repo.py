from typing import List, Optional

from src.product.entities import Product
from src.shared.contracts.repository import Repository


class ProductRepo(Repository):
    def get_all(self) -> List[Product]:
        """
        Retorna uma lista com todos os produtos
        :return: List[Product]
        """
        return list(Product.query.all())

    def get(self, product_id: int) -> Optional[Product]:
        """
        Retorna um produto pelo id

        Retorna None caso ele não exista
        :param product_id:
        :return: Optional[Product]
        """
        return Product.query.get(product_id)
