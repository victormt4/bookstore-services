from werkzeug.exceptions import BadRequest


class DomainError(BadRequest):
    def __init__(self, message: str):
        super().__init__(description=message)


class NotFoundError(DomainError):
    def __init__(self, message: str = 'Entity not found'):
        super().__init__(message)
