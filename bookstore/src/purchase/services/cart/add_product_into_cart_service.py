from bookstore.src.catalog import ProductServices
from bookstore.src.purchase.dto import ProductCart
from bookstore.src.purchase.errors import OutOfStockError
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter


class AddProductIntoCartService:
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