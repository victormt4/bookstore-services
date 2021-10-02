__version__ = '0.1.0'

from flask import Flask
from flask_restx import Api

from src.product.endpoints.product_endpoints import product_endpoint

api = Api(
    title='Bookstore Services',
    version=__version__,
    description='Rest services for bookStore app'
)

api.add_namespace(product_endpoint)

app = Flask(__name__)
api.init_app(app)
