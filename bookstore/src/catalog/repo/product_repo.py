from sqlalchemy.orm import Session

from bookstore.src.catalog.entities import Product
from bookstore.src.shared.contracts.repository import Repository


class ProductRepo(Repository[Product]):
    def __init__(self, database_session: Session):
        self._database_session = database_session

    def filter_by(self, **kwargs) -> list[Product]:
        return list(self._database_session.query(Product).filter_by(**kwargs))

    def get(self, product_id: int) -> Product | None:
        return self._database_session.query(Product).get(product_id)
