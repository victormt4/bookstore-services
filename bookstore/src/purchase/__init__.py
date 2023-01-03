from flask import session

from bookstore.database import get_database_session
from bookstore.src.catalog import CatalogServices
from bookstore.src.purchase.entities import Coupon
from bookstore.src.purchase.services.cart.add_product_into_cart_service import AddProductIntoCartService
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter
from bookstore.src.purchase.services.cart_services import CartServices as OldCartServices
from bookstore.src.purchase.services.checkout_services import CheckoutServices
from bookstore.src.purchase.services.coupon_services import CouponServices
from bookstore.src.shared.repository import Repository


class PurchaseServices:
    @staticmethod
    def get_cart_services() -> OldCartServices:
        return OldCartServices(
            CatalogServices.get_product_services(),
            session
        )

    @staticmethod
    def get_coupon_services() -> CouponServices:
        return CouponServices(
            Repository[Coupon](get_database_session(), Coupon),
            session
        )

    @classmethod
    def get_checkout_services(cls):
        return CheckoutServices(
            cls.get_cart_services(),
            cls.get_coupon_services()
        )


class CartServices:
    @staticmethod
    def get_add_product_into_cart_service():
        return AddProductIntoCartService(
            CartAdapter(session),
            CatalogServices.get_product_services()
        )
