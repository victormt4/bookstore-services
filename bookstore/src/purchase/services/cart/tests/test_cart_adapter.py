from unittest import TestCase
from pickle import loads
from uuid import uuid4

from bookstore.src.catalog import Product
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter


class CartAdapterTests(TestCase):
    def setUp(self) -> None:
        self._session = {}
        self._cart = CartAdapter(self._session)

    def test_add_product(self):
        product = self.__create_product_in_memory()
        quantity = 5

        self._cart.add_product(product, quantity)

        product_in_cart = self._cart.get_cart()[product.id]
        product_in_session = loads(self._session['cart'])[product.id]
        self.assertEqual(product_in_cart.quantity, quantity)
        self.assertEqual(product_in_session.quantity, quantity)

    def test_get_product(self):
        product = self.__create_product_in_memory()
        quantity = 5
        self._cart.add_product(product, quantity)

        product_into_cart = self._cart.get_product(product.id)

        self.assertEqual(product.id, product_into_cart.product.id)
        self.assertEqual(quantity, product_into_cart.quantity)

    def test_remove_product(self):
        product = self.__create_product_in_memory()
        self._cart.add_product(product, 5)

        self._cart.remove_product(product.id)

        self.assertIsNone(self._cart.get_cart().get(product.id))
        self.assertIsNone(loads(self._session['cart']).get(product.id))

    def test_remove_all(self):
        self._cart.add_product(self.__create_product_in_memory(), 5)
        self._cart.add_product(self.__create_product_in_memory(), 3)

        self._cart.remove_all()

        self.assertEqual({}, self._cart.get_cart())
        self.assertEqual({}, loads(self._session['cart']))

    def __create_product_in_memory(self) -> Product:
        product = Product(
            name='product',
            category='cat',
            description='desc',
            likes=5,
            price=5,
            picture='img.jpg',
            author='me',
            stock=5
        )
        product.id = uuid4().int
        return product
