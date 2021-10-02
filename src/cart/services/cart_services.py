from typing import Dict

from src.cart.dto import ProductCart
from src.cart.errors import OutOfStockError, NotFoundOnCartError
from src.product.services.product_services import ProductServices
from flask import session
import pickle


class CartServices:
    __cart_data: Dict[int, ProductCart]

    def __init__(self, product_services: ProductServices, session_object: session):
        self.__product_services = product_services
        self.__cart_data = {}
        self.__session_object = session_object
        if 'cart' in session_object:
            self.__cart_data = pickle.loads(session_object['cart'])

    def add_product_to_cart(self, product_id: int, quantity: int):
        product = self.__product_services.get_product(product_id)

        # Checando se o produto já está presente no carrinho, caso sim só incremente a quantidade atual
        if product.id in self.__cart_data:
            product_in_cart = self.__cart_data[product.id]
            product_in_cart.quantity = product_in_cart.quantity + quantity
        else:
            product_in_cart = ProductCart(product, quantity)

        if product.stock < product_in_cart.quantity:
            raise OutOfStockError(f"Out of stock for product #{product.id}")

        self.__cart_data[product.id] = product_in_cart

    def remove_product_from_cart(self, product_id: int, quantity: int):
        product = self.__product_services.get_product(product_id)

        if product.id not in self.__cart_data:
            raise NotFoundOnCartError(f"Product {product_id} not found in cart")

        quantity_in_cart = self.__cart_data[product.id].quantity
        new_quantity = quantity_in_cart - quantity

        # Caso o produto tenha sido zerado no carrinho, remova do dicionário
        if new_quantity <= 0:
            self.__cart_data.pop(product.id)
        else:
            self.__cart_data[product.id].quantity = new_quantity

    def clear_cart(self):
        self.__cart_data = {}

    def get_cart_data(self) -> Dict[int, ProductCart]:
        return self.__cart_data
