from typing import List, Optional
from json import load

from src.catalog.entities import Product
from src.purchase.entities import Coupon
from src.shared.contracts.repository import Repository, T


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

    def get(self, product_id: int) -> Optional[Product]:
        for product in self.get_all():
            if product.id == product_id:
                return product

        return None


class CouponRepoMock(Repository):

    def get_all(self) -> List[T]:
        with open('storage/coupons.json', 'r') as fp:
            return [
                Coupon(
                    coupon_dict['code'],
                    coupon_dict['discount']
                ) for coupon_dict in load(fp)
            ]

    def get(self, entity_id: int) -> Optional[T]:
        for coupon in self.get_all():
            if coupon.id == entity_id:
                return coupon

        return None
