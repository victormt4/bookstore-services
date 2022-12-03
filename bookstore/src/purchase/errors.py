from bookstore.src.shared.errors import DomainError


class OutOfStockError(DomainError):
    def __init__(self, message='Product of out stock'):
        super().__init__(message)


class NotFoundOnCartError(DomainError):
    def __init__(self, message: str = 'Product not found on cart'):
        super().__init__(message)


class CouponAlreadyActiveError(DomainError):
    def __init__(self, message: str = 'Coupon already active'):
        super().__init__(message)


class CouponLimitError(DomainError):
    def __init__(self, message: str = 'Coupon limit exceeded'):
        super().__init__(message)
