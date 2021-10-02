import pickle

import pytest

from src.cart.dto import ProductCart
from src.cart.errors import OutOfStockError, NotFoundOnCartError
from src.cart.services.cart_services import CartServices
from src.errors import NotFoundError
from src.product.services.product_services import ProductServices


def test_add_product_to_cart():
    cart = CartServices(ProductServices(), {})

    # Adiciona 15 produtos id = 1 e 1 produto id = 2
    cart.add_product_to_cart(1, 10)
    cart.add_product_to_cart(1, 5)
    cart.add_product_to_cart(2, 1)

    cart_data = cart.get_cart_data()

    assert 1 in cart_data
    assert cart_data[1].quantity == 15
    assert 2 in cart_data
    assert cart_data[2].quantity == 1

    # Tentando adicionar um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.add_product_to_cart(100, 1)

    # Tentando adicionar um produto com mais quantidade do que o disponível
    with pytest.raises(OutOfStockError):
        cart.add_product_to_cart(3, 10)


def test_remove_product_from_cart():
    # Criando um carrinho simulado dados serializados de uma sessão
    product_service = ProductServices()
    cart = CartServices(product_service, {
        'cart': pickle.dumps({
            1: ProductCart(product_service.get_product(1), 10),
            2: ProductCart(product_service.get_product(2), 5)
        })
    })

    # Remove 1 do produto id = 1, e remove o produto id = 2 por completo
    cart.remove_product_from_cart(1, 1)
    cart.remove_product_from_cart(2, 5)

    cart_data = cart.get_cart_data()

    assert cart_data[1].quantity == 9
    assert 2 not in cart_data

    # Tentando remover um produto que não existe no sistema
    with pytest.raises(NotFoundError):
        cart.remove_product_from_cart(100, 1)

    # Tentando remover um produto que não existe no carrinho
    with pytest.raises(NotFoundOnCartError):
        cart.remove_product_from_cart(3, 1)

    # Limpando carrinho
    cart.clear_cart()

    assert len(cart.get_cart_data()) == 0
