import pickle

import pytest

from src.cart.dto import ProductCart
from src.cart.errors import OutOfStockError, NotFoundOnCartError
from src.cart.services.cart_services import CartServices
from src.errors import NotFoundError


def test_add_product_to_cart(product_services):
    cart = CartServices(product_services, {})

    # Adiciona 15 produtos id = 1 e 1 produto id = 2
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(1, 5)
    cart.add_product_to_cart(2, 1)

    cart_data = cart.get_cart_data()

    assert 1 in cart_data
    assert cart_data[1].quantity == 15
    assert 2 in cart_data
    assert cart_data[2].quantity == 1

    cart.update_product_quantity(1, 5)

    assert cart.get_cart_data()[1].quantity == 5

    # Tentando adicionar um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.add_product_to_cart(100, 1)

    # Tentando adicionar um produto com mais quantidade do que o disponível
    with pytest.raises(OutOfStockError):
        cart.add_product_to_cart(3, 10)


def test_update_product_quantity(product_services):
    # Criando um carrinho simulado dados serializados de uma sessão
    cart = CartServices(product_services, {
        'cart': pickle.dumps({
            1: ProductCart(product_services.get_product(1), 10),
            2: ProductCart(product_services.get_product(2), 5)
        })
    })

    cart.update_product_quantity(1, 1)
    cart.update_product_quantity(2, 0)

    cart_data = cart.get_cart_data()

    assert cart_data[1].quantity == 1
    assert 2 not in cart_data

    # Tentando remover um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.update_product_quantity(100, 1)

    # Tentando remover um produto que não existe no carrinho
    with pytest.raises(NotFoundOnCartError):
        cart.update_product_quantity(3, 1)

    # Limpando carrinho
    cart.clear_cart()

    assert len(cart.get_cart_data()) == 0


def test_remove_product_from_cart(product_services):
    cart = CartServices(product_services, {
        'cart': pickle.dumps({
            1: ProductCart(product_services.get_product(1), 10),
            2: ProductCart(product_services.get_product(2), 5)
        })
    })

    cart.remove_product_from_cart(1)

    cart_data = cart.get_cart_data()

    assert 1 not in cart_data
    assert 2 in cart_data

    cart.remove_product_from_cart(2)

    assert 2 not in cart_data
