import pytest

from src.cart.errors import CouponLimitError
from src.cart.services.cart_services import CartServices
from src.cart.services.checkout_services import CheckoutServices
from src.cart.services.coupon_services import CouponServices
from src.product.services.product_services import ProductServices


def test_calc_subtotal():
    cart = CartServices(ProductServices(), {})
    checkout = CheckoutServices(cart, CouponServices({}))

    assert checkout.calc_sub_total() == 0

    # O valor do produto id = 1 custa 1.50 e o valor do produto id = 2 custa 2.50
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(2, 1)

    assert checkout.calc_sub_total() == 17.50

    # Removendo 1 produto do produto id = 1
    cart.update_product_quantity(1, 9)

    assert checkout.calc_sub_total() == 16.00

    # Removendo todos os produtos id = 1

    cart.update_product_quantity(1, 0)

    assert checkout.calc_sub_total() == 2.50

    # Limpando o carrinho

    cart.clear_cart()

    assert checkout.calc_sub_total() == 0


def test_calc_total():
    session = {}
    cart = CartServices(ProductServices(), session)
    coupon = CouponServices(session, 10)
    checkout = CheckoutServices(cart, coupon)

    cart.add_product_to_cart(1, 10)
    coupon.activate_coupon('ASD810dss9da!98')

    assert checkout.calc_sub_total() == 15.00
    assert checkout.calc_total() == 12.75

    # Tentando aplicar um desconto de 100%
    with pytest.raises(CouponLimitError):
        coupon.activate_coupon('asd1!98d10d98as')
        coupon.activate_coupon('asd1!19qdaasçs')
        checkout.calc_total()
