from src.errors import DomainError


class OutOfStockError(DomainError):
    def __init__(self, message='Product of out stock'):
        super().__init__(self, message)
