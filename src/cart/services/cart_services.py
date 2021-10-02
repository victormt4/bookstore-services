from src.cart.errors import OutOfStockError
from src.errors import NotFoundError
from src.product.services.product_services import ProductServices


class CartServices:
    def __init__(self, product_services: ProductServices, cart_data: dict):
        self.__product_services = product_services
        self.__cart_data = cart_data

    def add_product_to_cart(self, product_id: int, quantity: int):
        product = self.__product_services.get_product(product_id)

        # Checando se o produto já está presente no carrinho, caso sim só incremente a quantidade atual
        quantity_to_increase = quantity
        if product.id in self.__cart_data:
            quantity_in_cart = self.__cart_data[product.id]
            quantity_to_increase = quantity_in_cart + quantity

        if product.stock < quantity_to_increase:
            raise OutOfStockError(f"Out of stock for product #{product.id}")

        self.__cart_data[product.id] = quantity_to_increase

        return self

    def remove_product_from_cart(self, product_id: int, quantity: int):
        product = self.__product_services.get_product(product_id)

        if product.id not in self.__cart_data:
            raise NotFoundError(f"Product {product_id} not found in cart")

        quantity_in_cart = self.__cart_data[product.id]
        new_quantity = quantity_in_cart - quantity

        # Caso o produto tenha sido zerado no carrinho, remova do dicionário
        if new_quantity <= 0:
            self.__cart_data.pop(product.id)
        else:
            self.__cart_data[product.id] = new_quantity

        return self

    def get_cart_data(self) -> dict:
        return self.__cart_data
