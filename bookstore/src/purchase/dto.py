from money.money import Money
from money.currency import Currency
from bookstore.src.catalog.entities import Product


class ProductCart:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


class CheckoutTotals:
    def __init__(self, sub_total: int, total: int):
        self.sub_total = sub_total
        self.total = total
        self.sub_total_text = Money.from_sub_units(sub_total, Currency.BRL).format('pt_BR')
        self.total_text = Money.from_sub_units(total, Currency.BRL).format('pt_BR')
