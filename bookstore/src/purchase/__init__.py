from flask import session

from bookstore.database import get_database_session
from bookstore.src.catalog import CatalogServices
from bookstore.src.purchase.entities import Coupon
from bookstore.src.purchase.services.cart.add_or_update_product_into_cart_service import AddOrUpdateProductIntoCartService
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter
from bookstore.src.purchase.services.checkout.checkout_calculator_service import CheckoutCalculatorService
from bookstore.src.purchase.services.coupon_services import CouponServices
from bookstore.src.shared.repository import Repository


class PurchaseServices:
    @staticmethod
    def get_coupon_services() -> CouponServices:
        return CouponServices(
            Repository[Coupon](get_database_session(), Coupon),
            session
        )

    @classmethod
    def get_checkout_calculator_service(cls):
        return CheckoutCalculatorService(
            CartServices.get_cart_adapter(),
            cls.get_coupon_services()
        )


class CartServices:
    @staticmethod
    def get_add_or_update_product_into_cart_service() -> AddOrUpdateProductIntoCartService:
        return AddOrUpdateProductIntoCartService(
            CartAdapter(session),
            CatalogServices.get_product_services()
        )

    @staticmethod
    def get_cart_adapter() -> CartAdapter:
        return CartAdapter(session)
