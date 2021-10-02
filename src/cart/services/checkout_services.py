from functools import reduce
from src.cart.services.cart_services import CartServices


class CheckoutServices:
    def __init__(self, cart_services: CartServices):
        self.__cart = cart_services

    def calc_sub_total(self) -> float:
        """
        Calcula o sub total de todos os produtos do carrinho
        :return: float
        """
        cart_data = self.__cart.get_cart_data()
        return reduce(
            lambda total, current: (current.product.price * current.quantity) + total, cart_data.values(),
            0
        )
