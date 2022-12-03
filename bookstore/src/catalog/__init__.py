from bookstore.database import get_database_session
from bookstore.src.catalog.repo.product_repo import ProductRepo
from bookstore.src.catalog.services.product_services import ProductServices


class CatalogServices:
    @staticmethod
    def get_product_services() -> ProductServices:
        return ProductServices(
            ProductRepo(get_database_session())
        )
