from pickle import loads
from typing import Sequence

from bookstore.src.purchase.entities import Coupon
from bookstore.src.shared.contracts.repository_interface import RepositoryInterface
from bookstore.src.shared.errors import NotFoundError


class CouponQueryService:
    def __init__(self, coupon_repo: RepositoryInterface[Coupon], session: dict):
        self.__repo = coupon_repo
        self.__session = session

    def get_all_coupons(self) -> Sequence[Coupon]:
        return self.__repo.filter_by()

    def get_coupon_by_code(self, code: str) -> Coupon:
        if (coupon := self.__repo.get_by(code=code)) is None:
            raise NotFoundError(f'Coupon "{code}" not found')

        return coupon

    def get_active_coupons(self) -> dict[str, Coupon]:
        if 'active_coupons' not in self.__session:
            return {}

        return loads(self.__session['active_coupons'])
