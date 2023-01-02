from typing import TypeVar, Optional, Generic, Sequence

from sqlalchemy.orm import Session

from bookstore.src.shared.contracts.repository_interface import RepositoryInterface

Y = TypeVar('Y')


class Repository(Generic[Y], RepositoryInterface[Y]):
    def __init__(self, database_session: Session, entity_type: Y):
        self._database_session = database_session
        self._entity_type = entity_type

    def filter_by(self, **kwargs) -> Sequence[Y]:
        return self._database_session.query(self._entity_type).filter_by(**kwargs)

    def get(self, entity_id: int) -> Optional[Y]:
        return self._database_session.query(self._entity_type).get(entity_id)

    def create(self, **kwargs) -> Y:
        instance = self._entity_type(**kwargs)
        self._database_session.add(instance)
        self._database_session.flush([instance])
        return instance
