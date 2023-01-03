from pickle import dumps

from bookstore.src.purchase.errors import CouponAlreadyActiveError, CouponLimitError
from bookstore.src.purchase.services.coupon.coupon_query_service import CouponQueryService


class CouponActivatorService:
    def __init__(self, coupon_query_service: CouponQueryService, session_object: dict, coupon_limit: int = 1):
        self.__query_service = coupon_query_service
        self.__session = session_object
        self.__coupon_limit = coupon_limit

    def activate_coupon(self, code: str):
        coupon = self.__query_service.get_coupon_by_code(code)
        active_coupons = self.__query_service.get_active_coupons()

        if coupon.code in active_coupons:
            raise CouponAlreadyActiveError(f'Coupon "{code}" is already active')

        if len(active_coupons) == self.__coupon_limit:
            raise CouponLimitError(f"Coupon limit exceeded. Max coupons: {self.__coupon_limit}")

        active_coupons[coupon.code] = coupon
        self.__session['active_coupons'] = dumps(active_coupons)

    def deactivate_all_coupons(self):
        self.__session['active_coupons'] = dumps({})