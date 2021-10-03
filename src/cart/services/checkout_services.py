from src.cart.errors import CouponLimitError
from src.cart.services.cart_services import CartServices
from src.cart.services.coupon_services import CouponServices


class CheckoutServices:
    def __init__(self, cart_services: CartServices, coupon_services: CouponServices):
        """
        :param cart_services: CartServices
        :param coupon_services: CouponServices
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
        active_coupons = self.__coupon.get_active_coupons().values()

        discount_total = 0

        for coupon in active_coupons:
            discount_total += coupon.discount

        # Checando se o sistema não está tentando aplicar um limite de 100%
        if discount_total >= 1:
            raise CouponLimitError

        # TODO: Em uma situação real deve usar uma lib adequada para cálculos monetários
        total = self.calc_sub_total() * (1 - discount_total)

        return round(total, 2)
