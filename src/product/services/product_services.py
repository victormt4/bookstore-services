from json import load
from typing import List

from src.product.dto.product import Product


def get_product_list() -> List[Product]:
    """
    Return a list of Product
    :rtype: List[Product]
    """
    with open('storage/products.json', 'r') as fp:
        return [
            Product(
                product_dict['id'],
                product_dict['name'],
                product_dict['author'],
                product_dict['description'],
                product_dict['cover_picture'],
                product_dict['category'],
                product_dict['stock'],
                product_dict['users_who_liked']
            ) for product_dict in load(fp)
        ]
