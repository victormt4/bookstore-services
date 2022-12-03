from flask_restx import Api


def register_routes(app):
    from bookstore.src.catalog.endpoints.product_endpoints import product_endpoints
    from bookstore.src.purchase.endpoints.cart_endpoints import cart_endpoints
    from bookstore.src.purchase.endpoints.checkout_endpoints import checkout_endpoints

    # Configurando flask-restx
    api = Api(
        title='Bookstore Services',
        version='0.01',
        description='Endpoints para os serviços web do bookStore'
    )

    api.add_namespace(product_endpoints)
    api.add_namespace(cart_endpoints)
    api.add_namespace(checkout_endpoints)

    api.init_app(app)
