from sqlalchemy.orm import Session

from bookstore.src.catalog.entities import Product
from bookstore.src.shared.contracts.repository import Repository


class ProductRepo(Repository[Product]):
    def __init__(self, connection: Session):
        self._connection = connection

    def filter_by(self, **kwargs) -> list[Product]:
        return list(self._connection.query(Product).filter_by(**kwargs))

    def get(self, product_id: int) -> Product | None:
        return Product.query.get(product_id)
