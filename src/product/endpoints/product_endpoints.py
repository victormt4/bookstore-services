from flask_restx import Namespace, Resource, fields
from src.product.services.product_services import get_product_list

product_endpoint = Namespace('product', description='Product related operations', path='/product')

product_model = product_endpoint.model('Product', {
    'id': fields.Integer(required=True, description='Product id'),
    'name': fields.String(required=True, description='Product name')
})


@product_endpoint.route('/')
class ProductList(Resource):
    @product_endpoint.doc('list_products')
    @product_endpoint.marshal_list_with(product_model)
    def get(self):
        return [vars(product) for product in get_product_list()]
