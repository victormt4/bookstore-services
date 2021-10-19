from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional, Generic

T = TypeVar('T')


class Repository(Generic[T], ABC):

    @abstractmethod
    def get_all(self) -> List[T]:
        """
        Deve retornar todos os registros da entidade T
        :return: List[T]
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        """
        Deve retornar um único registro para o id da entidade T informado, ou None caso não exista
        :param entity_id: int
        :return: Optional[T]
        """
        raise NotImplementedError
