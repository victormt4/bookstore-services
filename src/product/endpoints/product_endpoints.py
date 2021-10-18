from flask_restx import Namespace, Resource, fields
from src.product.services.product_services import ProductServices



product_endpoints = Namespace('product', description='Endpoints relacionados aos produtos da loja', path='/product')

product_model = product_endpoints.model('Product', {
    'id': fields.Integer(required=True, description='Id'),
    'name': fields.String(required=True, description='Nome'),
    'author': fields.String(required=True, description='Autor/fabricante do produto'),
    'description': fields.String(required=True, description='Descrição do produto'),
    'picture': fields.String(required=True, description='Url da imagem', example='https://image.com/livro.jpg'),
    'category': fields.String(required=True, description='Categoria', example='Manga'),
    'stock': fields.Integer(required=True, description='Quantidade em estoque,'),
    'price': fields.Integer(required=True, description='Preço do produto em centavos', example=150),
    'priceText': fields.String(required=True, description='Preço do produto formatado em reais', example='R$ 1,50'),
    'likes': fields.Integer(required=False, default=0, description='Quantidade de likes')
})


@product_endpoints.route('')
class ProductList(Resource):
    def __init__(self, *args, **kwargs):
        self.__services = ProductServices()
        super().__init__(*args, **kwargs)

    @product_endpoints.doc(description='Retorna uma lista de produtos')
    @product_endpoints.marshal_list_with(product_model)
    def get(self):
        return [vars(product) for product in self.__services.get_product_list()]
