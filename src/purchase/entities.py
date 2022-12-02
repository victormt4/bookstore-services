from bookstore import db


class Coupon(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String, nullable=False)
    discount = db.Column(db.Float, nullable=False)

    def __init__(self, code: str, discount: float):
        self.code = code
        self.discount = discount
