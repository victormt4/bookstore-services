from abc import ABC, abstractmethod
from typing import TypeVar, Optional, Generic, Sequence

T = TypeVar('T')


class RepositoryInterface(Generic[T], ABC):
    @abstractmethod
    def filter_by(self, **kwargs) -> Sequence[T]:
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def create(self, **kwargs) -> T:
        raise NotImplementedError
