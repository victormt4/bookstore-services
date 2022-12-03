from sqlalchemy.orm import Session

from bookstore.src.purchase.entities import Coupon
from bookstore.src.shared.contracts.repository import Repository


class CouponRepo(Repository[Coupon]):
    def __init__(self, database_session: Session):
        self._database_session = database_session

    def filter_by(self, **kwargs) -> list[Coupon]:
        return list(self._database_session.query(Coupon).filter_by(**kwargs))

    def get(self, coupon_id: int) -> Coupon | None:
        return self._database_session.query(Coupon).get(coupon_id)
