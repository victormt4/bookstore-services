from sqlalchemy import Table, Column, Integer, String, BigInteger
from sqlalchemy.orm import mapper
from money.money import Money
from money.currency import Currency

from bookstore.database import metadata


class Product(object):
    id: int

    def __init__(self, name: str, author: str, description: str, picture: str, category: str,
                 stock: int,
                 likes: int, price):
        self.name = name
        self.author = author
        self.description = description
        self.picture = picture
        self.category = category
        self.stock = stock
        self.likes = likes
        self.price = price

    @property
    def price_text(self) -> Money:
        return Money.from_sub_units(self.price, Currency.BRL).format('pt_BR')


_product_table = Table(
    'product',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String(length=255), nullable=False),
    Column('author', String(length=255), nullable=False),
    Column('description', String, nullable=False),
    Column('picture', String(length=255), nullable=False),
    Column('category', String(length=255), nullable=False),
    Column('stock', Integer, nullable=False),
    Column('likes', Integer, nullable=False),
    Column('price', BigInteger, nullable=False),
)

mapper(Product, _product_table)
