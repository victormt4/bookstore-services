from flask import session

from bookstore.database import get_database_session
from bookstore.src.catalog import CatalogServices
from bookstore.src.purchase.repo.coupon_repo import CouponRepo
from bookstore.src.purchase.services.cart_services import CartServices
from bookstore.src.purchase.services.checkout_services import CheckoutServices
from bookstore.src.purchase.services.coupon_services import CouponServices


class PurchaseServices:
    @staticmethod
    def get_cart_services() -> CartServices:
        return CartServices(
            CatalogServices.get_product_services(),
            session
        )

    @staticmethod
    def get_coupon_services() -> CouponServices:
        return CouponServices(
            CouponRepo(get_database_session()),
            session
        )

    @classmethod
    def get_checkout_services(cls):
        return CheckoutServices(
            cls.get_cart_services(),
            cls.get_coupon_services()
        )
