from src.catalog.entities import Product
from src.shared.contracts.repository import Repository


class ProductRepo(Repository[Product]):
    def filter_by(self, **kwargs) -> list[Product]:
        return list(Product.query.filter_by(**kwargs))

    def get(self, product_id: int) -> Product | None:
        return Product.query.get(product_id)
