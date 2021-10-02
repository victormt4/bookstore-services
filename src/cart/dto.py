from src.product.entities import Product


class ProductCart:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
