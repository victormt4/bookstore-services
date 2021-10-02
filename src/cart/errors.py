from src.errors import DomainError, NotFoundError


class OutOfStockError(DomainError):
    def __init__(self, message='Product of out stock'):
        super().__init__(self, message)


class NotFoundOnCartError(DomainError):
    def __init__(self, message: str = 'Product not found on cart'):
        super().__init__(self, message)


class CouponAlreadyActiveError(DomainError):
    def __init__(self, message: str = 'Coupon already active'):
        super().__init__(self, message)
