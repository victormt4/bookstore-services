import pytest

from src.cart.errors import OutOfStockError
from src.cart.services.cart_services import CartServices
from src.errors import NotFoundError
from src.product.services.product_services import ProductServices


def test_add_product_to_cart():
    cart = CartServices(ProductServices(), {2: 0})

    # Adiciona 15 produtos id = 1 e 1 produto id = 2
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(1, 5)
    cart.add_product_to_cart(2, 1)

    cart_data = cart.get_cart_data()

    assert 1 in cart_data
    assert cart_data[1] == 15
    assert 2 in cart_data
    assert cart_data[2] == 1

    # Tentando adicionar um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.add_product_to_cart(100, 1)

    # Tentando adicionar um produto com mais quantidade do que o disponível
    with pytest.raises(OutOfStockError):
        cart.add_product_to_cart(3, 10)


def test_remove_product_from_cart():
    cart = CartServices(ProductServices(), {1: 10, 2: 5})

    # Remove 1 do produto id = 1, e remove o produto id = 2 por completo
    cart.remove_product_from_cart(1, 1)
    cart.remove_product_from_cart(2, 5)

    cart_data = cart.get_cart_data()

    assert cart_data[1] == 9
    assert 2 not in cart_data

    # Tentando remover um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.remove_product_from_cart(100, 1)

    # Tentando adicionar um produto que não existe no carrinho
    with pytest.raises(NotFoundError):
        cart.remove_product_from_cart(3, 1)
