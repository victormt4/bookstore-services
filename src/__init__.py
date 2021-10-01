__version__ = '0.1.0'

from flask import Flask
from src.product.blueprints.product_list_blueprint import product_list_blueprint

app = Flask(__name__)

app.register_blueprint(product_list_blueprint, url_prefix='/api/v1')
