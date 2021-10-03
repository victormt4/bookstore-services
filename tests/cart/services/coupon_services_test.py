import pytest

from src.cart.entities import Coupon
from src.cart.errors import CouponAlreadyActiveError, CouponLimitError
from src.cart.services.coupon_services import CouponServices
from src.errors import NotFoundError


def test_get_coupons():
    coupon_service = CouponServices({})

    coupons = coupon_service.get_coupons()

    assert type(coupons) == list
    assert len(coupons) == 4
    for coupon in coupons:
        assert type(coupon) == Coupon


def test_get_coupon():
    coupon_service = CouponServices({})

    assert coupon_service.get_coupon('ASD810dss9da!98').code == 'ASD810dss9da!98'

    # Tentando buscar um coupon que não existe
    with pytest.raises(NotFoundError):
        coupon_service.get_coupon('JASLKDJALKDJSKLA')


def test_activate_coupon():
    coupon_service = CouponServices({}, 10)

    coupon_service.activate_coupon('ASD810dss9da!98')
    coupon_service.activate_coupon('4asd12d1asd!98')

    coupons = coupon_service.get_active_coupons()

    assert len(coupons) == 2
    assert 'ASD810dss9da!98' in coupons
    assert '4asd12d1asd!98' in coupons

    with pytest.raises(CouponAlreadyActiveError):
        coupon_service.activate_coupon('ASD810dss9da!98')

    coupon_service = CouponServices({}, 1)
    coupon_service.activate_coupon('ASD810dss9da!98')

    # Tentando ativar um coupon acima do limite permitido
    with pytest.raises(CouponLimitError):
        coupon_service.activate_coupon('4asd12d1asd!98')
