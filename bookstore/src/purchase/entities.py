from sqlalchemy import Table, Column, Float, String, BigInteger
from sqlalchemy.orm import mapper


from bookstore.database import metadata


class Coupon(object):
    id: int

    def __init__(self, code: str, discount: float):
        self.code = code
        self.discount = discount


_coupon_table = Table(
    'coupon',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('code', String, primary_key=True, autoincrement=True),
    Column('discount', Float, primary_key=True, autoincrement=True),
)

mapper(Coupon, _coupon_table)