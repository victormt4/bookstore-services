from typing import List

from src.errors import NotFoundError
from src.product.entities import Product


class ProductServices:

    def get_product_list(self) -> List[Product]:
        """
        Return a list of Product
        :rtype: List[Product]
        """
        return list(Product.query.all())


    def get_product(self, product_id: int) -> Product:
        """
        Get a product by id
        :rtype: Product
        :raises NotFoundError
        """
        product = Product.query.get(product_id)

        if product is None:
            raise NotFoundError(f"Product #{product_id} not found")

        return product
