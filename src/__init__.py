__version__ = '0.1.0'

from os import getenv, urandom

from dotenv import load_dotenv

from flask import Flask
from flask_restx import Api

from src.product.endpoints.product_endpoints import product_endpoints
from src.cart.endpoints.cart_endpoints import cart_endpoints
from src.cart.endpoints.checkout_endpoints import checkout_endpoints

# Carregando variáveis de ambiente
load_dotenv()

# Configurando flask
app = Flask(__name__)
app.secret_key = getenv('FLASK_SECRET_KEY', urandom(16))
app.config['RESTX_VALIDATE'] = True

# Configurando flask-restx
api = Api(
    title='Bookstore Services',
    version=__version__,
    description='Endpoints para os serviços web do bookStore'
)

api.add_namespace(product_endpoints)
api.add_namespace(cart_endpoints)
api.add_namespace(checkout_endpoints)
api.init_app(app)
