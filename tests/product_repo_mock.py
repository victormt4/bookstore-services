from typing import List
from json import load

from src.errors import NotFoundError
from src.catalog.entities import Product
from src.shared.contracts.repository import Repository


class ProductRepoMock(Repository):

    def get_all(self) -> List[Product]:
        with open('storage/products.json', 'r') as fp:
            product_list = []
            for product_dict in load(fp):
                p = Product(
                    product_dict['name'],
                    product_dict['author'],
                    product_dict['description'],
                    product_dict['cover_picture'],
                    product_dict['category'],
                    product_dict['stock'],
                    len(product_dict['users_who_liked']),
                    product_dict['id'] * 100
                )
                p.id = product_dict['id']
                product_list.append(p)

            return product_list

    def get(self, product_id: int) -> Product:
        for product in self.get_all():
            if product.id == product_id:
                return product

        raise NotFoundError(f"Product #{product_id} not found")
