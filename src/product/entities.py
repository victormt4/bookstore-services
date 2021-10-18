from typing import List
from money.money import Money
from money.currency import Currency

from src import db


class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    likes = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.BigInteger, nullable=False, default=0)

    def __init__(self, product_id: int, name: str, author: str, description: str, picture: str, category: str,
                 stock: int,
                 users_who_liked: List[str]):
        self.id = product_id
        self.name = name
        self.author = author
        self.description = description
        self.picture = picture
        self.category = category
        self.stock = stock
        self.users_who_liked = users_who_liked
        self.likes = len(users_who_liked)
        self.price = product_id * 100
        self.priceText = Money.from_sub_units(self.price, Currency.BRL).format('pt_BR')
