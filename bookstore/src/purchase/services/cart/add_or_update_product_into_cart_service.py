from typing import Optional

from bookstore.src.catalog import ProductServices
from bookstore.src.purchase.dto import ProductCart
from bookstore.src.purchase.errors import OutOfStockError, NotFoundOnCartError
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter


class AddOrUpdateProductIntoCartService:
    def __init__(self, cart: CartAdapter, product_services: ProductServices):
        self.__cart = cart
        self.__product_services = product_services

    def add_product_to_cart(self, product_id: int, quantity: int) -> ProductCart:
        product = self.__product_services.get_product(product_id)

        if product_in_cart := self.__cart.get_product(product.id):
            quantity = product_in_cart.quantity + quantity

        if product.stock < quantity:
            raise OutOfStockError(f"Out of stock for product #{product.id}")

        return self.__cart.add_product(product, quantity)

    def update_product_quantity(self, product_id: int, quantity: int) -> Optional[ProductCart]:
        product = self.__product_services.get_product(product_id)

        if (product_in_cart := self.__cart.get_product(product.id)) is None:
            raise NotFoundOnCartError(f"Product #{product_id} not found in cart")

        if quantity <= 0:
            return self.__cart.remove_product(product_id)

        new_quantity = quantity + product_in_cart.quantity
        if product.stock < new_quantity:
            raise OutOfStockError(f"Out of stock for product #{product.id}")

        return self.__cart.add_product(product, new_quantity)

    def remove_product_from_cart(self, product_id: int):
        product = self.__product_services.get_product(product_id)

        if (product_in_cart := self.__cart.get_product(product.id)) is None:
            raise NotFoundOnCartError(f"Product #{product_id} not found in cart")

        self.__cart.remove_product(product_id)