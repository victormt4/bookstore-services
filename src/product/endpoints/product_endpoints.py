from flask_restx import Namespace, Resource, fields
from src.product.services.product_services import ProductServices

product_endpoint = Namespace('product', description='Endpoints relacionados aos produtos da loja', path='/product')

product_model = product_endpoint.model('Product', {
    'id': fields.Integer(required=True, description='Id'),
    'name': fields.String(required=True, description='Nome'),
    'author': fields.String(required=True, description='Autor/fabricante do produto'),
    'picture': fields.String(required=True, description='Url da imagem'),
    'category': fields.String(required=True, description='Categoria'),
    'stock': fields.Integer(required=True, description='Quantidade em estoque,'),
    'price': fields.Float(required=True, description='Preço'),
    'likes': fields.Integer(required=False, default=0, description='Quantidade de likes')
})


@product_endpoint.route('/')
class ProductList(Resource):
    def __init__(self, *args, **kwargs):
        self.__services = ProductServices()
        super().__init__(*args, **kwargs)

    @product_endpoint.marshal_list_with(product_model, description='Retorna uma lista de produtos')
    def get(self):
        return [vars(product) for product in self.__services.get_product_list()]