class DomainError(Exception):
    pass


class NotFoundError(DomainError):
    def __init__(self, message: str = 'Entity not found'):
        super().__init__(self, message)
