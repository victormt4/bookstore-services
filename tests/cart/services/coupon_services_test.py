import pytest

from src.cart.entities import Coupon
from src.cart.services.coupon_service import CouponService
from src.errors import NotFoundError


def test_get_coupons():
    coupon_service = CouponService()

    coupons = coupon_service.get_coupons()

    assert type(coupons) == list
    assert len(coupons) == 3
    for coupon in coupons:
        assert type(coupon) == Coupon


def test_get_coupon():
    coupon_service = CouponService()

    assert coupon_service.get_coupon('ASD810dss9da!98').code == 'ASD810dss9da!98'

    # Tentando buscar um coupon que não existe
    with pytest.raises(NotFoundError):
        coupon_service.get_coupon('JASLKDJALKDJSKLA')
