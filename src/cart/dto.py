from src.product.entities import Product


class ProductCart:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


class CheckoutTotals:
    def __init__(self, sub_total: float, total: float):
        self.sub_total = sub_total
        self.total = total
