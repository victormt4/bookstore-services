from src.cart.services.cart_services import CartServices
from src.cart.services.coupon_services import CouponServices


class CheckoutServices:
    def __init__(self, cart_services: CartServices, coupon_services: CouponServices):
        """
        :param cart_services: CartServices
        """
        self.__cart = cart_services
        self.__coupon = coupon_services

    def calc_sub_total(self) -> float:
        """
        Calcula o sub total de todos os produtos do carrinho
        :return: float
        """
        cart_data = self.__cart.get_cart_data()
        return sum(product_in_cart.product.price * product_in_cart.quantity for product_in_cart in cart_data.values())

    def calc_total(self) -> float:
        """
        Calcula o total de todos os produtos do carrinho (Aplicando coupons, fretes, outras taxas)
        :return: float
        """
        sub_total = self.calc_sub_total()

        total = sub_total

        return total


