__version__ = '0.1.0'

from flask import Flask
from flask_restx import Api

from src.product.endpoints.product_endpoints import product_endpoints
from src.cart.endpoints.cart_endpoints import cart_endpoints

api = Api(
    title='Bookstore Services',
    version=__version__,
    description='Endpoints para os serviços web do bookStore'
)

api.add_namespace(product_endpoints)
api.add_namespace(cart_endpoints)

app = Flask(__name__)
api.init_app(app)
