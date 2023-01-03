from pickle import loads, dumps
from typing import Optional

from bookstore.src.catalog import Product
from bookstore.src.purchase.dto import ProductCart


class CartAdapter:
    __cart_data: dict[int, ProductCart]

    def __init__(self, session: dict):
        self.__cart_data = {}
        self.__session_object = session
        if 'cart' in session:
            self.__cart_data = loads(session['cart'])

    def add_product(self, product: Product, quantity: int) -> ProductCart:
        product_cart = ProductCart(product, quantity)
        self.__cart_data[product.id] = product_cart
        self.__update_session()
        return product_cart

    def remove_product(self, product_id: int):
        self.__cart_data.pop(product_id)
        self.__update_session()

    def remove_all(self):
        self.__cart_data = {}
        self.__update_session()

    def get_product(self, product_id: int) -> Optional[ProductCart]:
        return self.__cart_data.get(product_id)

    def get_cart(self) -> dict[int, ProductCart]:
        return self.__cart_data

    def __update_session(self):
        self.__session_object['cart'] = dumps(self.__cart_data)


