from flask import session
from flask_restx import Namespace, Resource, fields

from src.cart.services.cart_services import CartServices
from src.product.services.product_services import ProductServices
from src.product.endpoints.product_endpoints import product_model

cart_endpoints = Namespace('cart', description='Endpoints para operações no carrinho da loja', path='/cart')

product_cart_model = cart_endpoints.model('ProductCart', {
    'product': fields.Nested(product_model),
    'quantity': fields.Integer(required=True, min=0, description='Quantidade de produtos no carrinho')
})


@cart_endpoints.route('/')
class Cart(Resource):
    def __init__(self, *args, **kwargs):
        self.__cart_service = CartServices(
            ProductServices(),
            session
        )
        super().__init__(*args, **kwargs)

    @cart_endpoints.marshal_list_with(product_cart_model, description='Lista de produtos no carrinho de compras')
    def get(self):
        cart_data = self.__cart_service.get_cart_data().values()
        if len(cart_data):
            return cart_data
        return []
