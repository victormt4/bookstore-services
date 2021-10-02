from typing import List
from json import load

from src.cart.entities import Coupon
from src.errors import NotFoundError


class CouponService:
    def get_coupons(self) -> List[Coupon]:
        """
        Retorna uma lista de coupons
        :rtype: List[Coupon]
        """
        with open('storage/coupons.json', 'r') as fp:
            return [
                Coupon(
                    coupon_dict['code'],
                    coupon_dict['discount']
                ) for coupon_dict in load(fp)
            ]

    def get_coupon(self, code: str) -> Coupon:
        """
        Busca um coupon pelo código
        :rtype: Coupon
        """
        coupons = self.get_coupons()

        for coupon in coupons:
            if coupon.code == code:
                return coupon

        raise NotFoundError(f"Coupon #{code} not found")
