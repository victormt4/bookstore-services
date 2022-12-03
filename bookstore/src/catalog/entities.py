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
    Column('name', String, primary_key=True, autoincrement=True),
    Column('author', String, primary_key=True, autoincrement=True),
    Column('description', String, primary_key=True, autoincrement=True),
    Column('picture', String, primary_key=True, autoincrement=True),
    Column('category', String, primary_key=True, autoincrement=True),
    Column('stock', Integer, primary_key=True, autoincrement=True),
    Column('likes', Integer, primary_key=True, autoincrement=True),
    Column('price', BigInteger, primary_key=True, autoincrement=True),
)

mapper(Product, _product_table)
