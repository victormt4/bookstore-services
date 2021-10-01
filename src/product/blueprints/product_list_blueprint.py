from flask import Blueprint, jsonify
from src.product.services.product_services import get_product_list

product_list_blueprint = Blueprint(name='product_list_blueprint', import_name=__name__)


@product_list_blueprint.route('/products', methods=['GET'])
def products():
    return jsonify([vars(product) for product in get_product_list()])
