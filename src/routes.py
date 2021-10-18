from src import __version__

from flask_restx import Api


def register_routes(app):
    from src.product.endpoints.product_endpoints import product_endpoints
    from src.cart.endpoints.cart_endpoints import cart_endpoints
    from src.cart.endpoints.checkout_endpoints import checkout_endpoints

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
