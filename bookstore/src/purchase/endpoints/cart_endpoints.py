from flask_restx import Namespace, Resource, fields

from bookstore.src.purchase import CartServices
from bookstore.src.catalog.endpoints.product_endpoints import product_model

cart_endpoints = Namespace('cart', description='Endpoints para operações no carrinho da loja', path='/cart')

product_cart_model = cart_endpoints.model('ProductCart', {
    'product': fields.Nested(product_model),
    'quantity': fields.Integer(required=True, min=0, description='Quantidade de produtos no carrinho')
})

product_cart_input_model = cart_endpoints.model('ProductCartInput', {
    'productId': fields.Integer(required=True, description='Id do produto', example=13718),
    'quantity': fields.Integer(required=True, min=1, description='Quantidade do produto a ser adicionado')
})

product_cart_input_parser = cart_endpoints.parser()
product_cart_input_parser.add_argument('productId', type=int, location='json')
product_cart_input_parser.add_argument('quantity', type=int, location='json')


class DefaultEndpoint(Resource):
    def __init__(self, *args, **kwargs):
        self._cart_service = CartServices.get_add_or_update_product_into_cart_service()
        self._cart_adapter = CartServices.get_cart_adapter()
        super().__init__(*args, **kwargs)


@cart_endpoints.route('')
class CartList(DefaultEndpoint):

    @cart_endpoints.doc(description='Lista os produtos do carrinho de compras')
    @cart_endpoints.marshal_list_with(product_cart_model)
    def get(self):
        cart_data = list(self._cart_adapter.get_cart().values())
        if len(cart_data):
            return cart_data
        return []

    @cart_endpoints.doc(body=product_cart_input_model, description='Adiciona um produto no carrinho')
    def post(self):
        request_input = product_cart_input_parser.parse_args()
        self._cart_service.add_product_to_cart(
            request_input.get('productId'),
            request_input.get('quantity')
        )
        return {'message': 'Product added to cart'}

    @cart_endpoints.doc(body=product_cart_input_model, description='Atualiza a quantidade do produto no carrinho')
    def put(self):
        request_input = product_cart_input_parser.parse_args()
        self._cart_service.update_product_quantity(
            request_input.get('productId'),
            request_input.get('quantity')
        )
        return {'message': 'Product quantity has been updated'}

    @cart_endpoints.doc(description='Limpa todos os dados do carrinho')
    def delete(self):
        self._cart_adapter.remove_all()
        return {'message': 'All products have been removed from the cart'}


@cart_endpoints.route('/<int:product_id>')
class Cart(DefaultEndpoint):

    @cart_endpoints.doc(description='Remove um produto do carrinho', params={'product_id': 'Id do produto'})
    def delete(self, product_id):
        self._cart_service.remove_product_from_cart(product_id)
        return {'message': 'Product has been removed'}
