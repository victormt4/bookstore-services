from json import load

from bookstore.database import get_database_session


def register_commands(app):
    @app.cli.command("seed")
    def seed():
        """
        Insere os produtos no banco de dados
        """
        from bookstore.src.catalog.entities import Product
        from bookstore.src.purchase.entities import Coupon

        print('\nSeeding...')

        # Criando produtos
        with open('storage/products.json', 'r') as fp:
            db = get_database_session()

            for product_dict in load(fp):
                p = Product(
                    product_dict['name'],
                    product_dict['author'],
                    product_dict['description'],
                    product_dict['cover_picture'],
                    product_dict['category'],
                    product_dict['stock'],
                    len(product_dict['users_who_liked']),
                    product_dict['id'] * 100
                )
                db.add(p)

        # Criando coupons
        with open('storage/coupons.json', 'r') as fp:
            for coupon_dict in load(fp):
                c = Coupon(
                    coupon_dict['code'],
                    coupon_dict['discount']
                )
                db.add(c)

        # Comitando alterações
        db.commit()
