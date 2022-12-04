from bookstore.database import get_database_session
from bookstore.src.catalog.entities import Product
from bookstore.src.catalog.services.product_services import ProductServices
from bookstore.src.shared.repository import Repository


class CatalogServices:
    @staticmethod
    def get_product_services() -> ProductServices:
        return ProductServices(
            Repository[Product](get_database_session(), Product)
        )
