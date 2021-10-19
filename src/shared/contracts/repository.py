from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Generic

T = TypeVar('T')


class Repository(Generic[T], ABC):

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        raise NotImplementedError
