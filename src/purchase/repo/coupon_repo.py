from typing import Optional, List

from src.purchase.entities import Coupon
from src.shared.contracts.repository import Repository


class CouponRepo(Repository[Coupon]):
    def filter_by(self, **kwargs) -> List[Coupon]:
        return Coupon.query.filter_by(**kwargs)

    def get(self, coupon_id: int) -> Optional[Coupon]:
        return Coupon.query.get(coupon_id)
