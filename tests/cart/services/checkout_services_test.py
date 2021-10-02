from src.cart.services.cart_services import CartServices
from src.cart.services.checkout_services import CheckoutServices
from src.product.services.product_services import ProductServices


def test_calc_subtotal():
    cart = CartServices(ProductServices(), {})
    checkout = CheckoutServices(cart)

    assert checkout.calc_sub_total() == 0

    # O valor do produto id = 1 custa 1.50 e o valor do produto id = 2 custa 2.50
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(2, 1)

    assert checkout.calc_sub_total() == 17.50

    # Removendo 1 produto do produto id = 1
    cart.remove_product_from_cart(1, 1)

    assert checkout.calc_sub_total() == 16.00

    # Removendo todos os produtos id = 1

    cart.remove_product_from_cart(1, 9)

    assert checkout.calc_sub_total() == 2.50

    # Limpando o carrinho

    cart.clear_cart()

    assert checkout.calc_sub_total() == 0
