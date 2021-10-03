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

product_cart_input_model = cart_endpoints.model('ProductCartInput', {
    'productId': fields.Integer(required=True, description='Id do produto', example=13718),
    'quantity': fields.Integer(required=True, min=1, description='Quantidade do produto a ser adicionado')
})


@cart_endpoints.route('')
class Cart(Resource):
    def __init__(self, *args, **kwargs):
        self.__cart_service = CartServices(
            ProductServices(),
            session
        )
        super().__init__(*args, **kwargs)

    @cart_endpoints.marshal_list_with(product_cart_model, description='Lista de produtos no carrinho de compras')
    def get(self):
        cart_data = list(self.__cart_service.get_cart_data().values())
        if len(cart_data):
            return cart_data
        return []

    @cart_endpoints.doc(body=product_cart_input_model, description='Adiciona um produto no carrinho')
    def post(self):
        parser = cart_endpoints.parser()
        parser.add_argument('productId', type=int, location='json')
        parser.add_argument('quantity', type=int, location='json')
        args = parser.parse_args()
        self.__cart_service.add_product_to_cart(
            args.get('productId'),
            args.get('quantity')
        )
        return {'message': 'Produto adicionado'}
