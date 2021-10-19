from typing import Optional, List

from src.purchase.entities import Coupon
from src.shared.contracts.repository import Repository


class CouponRepo(Repository):
    def get_all(self) -> List[Coupon]:
        return Coupon.query.all()

    def get(self, coupon_id: int) -> Optional[Coupon]:
        return Coupon.query.get(coupon_id)
