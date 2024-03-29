from functools import reduce
from money.money import Money
from money.currency import Currency

from bookstore.src.purchase import CartAdapter
from bookstore.src.purchase.dto import CheckoutTotals
from bookstore.src.purchase.errors import CouponLimitError
from bookstore.src.purchase.services.coupon.coupon_query_service import CouponQueryService


class CheckoutCalculatorService:
    def __init__(self, cart: CartAdapter, coupon_query_service: CouponQueryService):
        self.__cart = cart
        self.__coupon_query_service = coupon_query_service

    def calc_sub_total(self) -> int:
        cart_data = self.__cart.get_cart()

        def sum_func(total_sum, current):
            price = Money.from_sub_units(current.product.price, Currency.BRL)
            return total_sum + (price * current.quantity).sub_units

        total = reduce(sum_func, cart_data.values(), 0)
        return total

    def calc_total(self) -> int:
        active_coupons = self.__coupon_query_service.get_active_coupons().values()

        discount_total = 0

        for coupon in active_coupons:
            discount_total += coupon.discount

        if discount_total >= 1:
            raise CouponLimitError

        total = Money.from_sub_units(self.calc_sub_total(), Currency.BRL) * (1 - discount_total)

        return total.sub_units

    def get_totals(self) -> CheckoutTotals:
        return CheckoutTotals(self.calc_sub_total(), self.calc_total())
