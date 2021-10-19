import pytest

from src.purchase.errors import CouponLimitError
from src.purchase.services.cart_services import CartServices
from src.purchase.services.checkout_services import CheckoutServices
from src.purchase.services.coupon_services import CouponServices


def test_calc_subtotal(product_services, coupon_repo):
    cart = CartServices(product_services, {})
    checkout = CheckoutServices(cart, CouponServices(coupon_repo, {}))

    assert checkout.calc_sub_total() == 0

    # O valor do produto id = 1 custa 100 centavos e o valor do produto id = 2 custa 200 centavos
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(2, 1)

    assert checkout.calc_sub_total() == 1200

    # Removendo 1 produto do produto id = 1
    cart.update_product_quantity(1, 9)

    assert checkout.calc_sub_total() == 1100

    # Removendo todos os produtos id = 1

    cart.update_product_quantity(1, 0)

    assert checkout.calc_sub_total() == 200

    # Limpando o carrinho

    cart.clear_cart()

    assert checkout.calc_sub_total() == 0


def test_calc_total(product_services, coupon_repo):
    session = {}
    cart = CartServices(product_services, session)
    coupon = CouponServices(coupon_repo, session, 10)
    checkout = CheckoutServices(cart, coupon)

    cart.add_product_to_cart(1, 10)
    # Adicionando cupom de 15% de desconto
    coupon.activate_coupon('ASD810dss9da!98')

    assert checkout.calc_sub_total() == 1000
    assert checkout.calc_total() == 850

    # Tentando aplicar um desconto de 100%
    with pytest.raises(CouponLimitError):
        coupon.activate_coupon('asd1!98d10d98as')
        coupon.activate_coupon('asd1!19qdaasçs')
        checkout.calc_total()
