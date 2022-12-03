from typing import List, Optional
from json import load

from bookstore.src.catalog.entities import Product
from bookstore.src.purchase.entities import Coupon
from bookstore.src.shared.contracts.repository import Repository, T


class ProductRepoMock(Repository):

    def filter_by(self) -> List[Product]:
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
        for product in self.filter_by():
            if product.id == product_id:
                return product

        return None


class CouponRepoMock(Repository):

    def filter_by(self) -> List[T]:
        with open('storage/coupons.json', 'r') as fp:
            return [
                Coupon(
                    coupon_dict['code'],
                    coupon_dict['discount']
                ) for coupon_dict in load(fp)
            ]

    def get(self, entity_id: int) -> Optional[T]:
        for coupon in self.filter_by():
            if coupon.id == entity_id:
                return coupon

        return None
