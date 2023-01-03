from bookstore.src.catalog import Product, CatalogServices
from bookstore.src.purchase import AddProductIntoCartService, CartAdapter
from bookstore.src.purchase.errors import OutOfStockError
from bookstore.src.shared.repository import Repository
from bookstore.tests.test_cases.IntegrationTestCase import IntegrationTestCase


class AddProductIntoCartServiceTests(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.__product_repo = Repository[Product](self.db_connection, Product)
        self.__cart_adapter = CartAdapter({})
        self.__service = AddProductIntoCartService(
            self.__cart_adapter,
            CatalogServices.get_product_services()
        )

    def test_add_product_to_cart(self):
        product = self.__create_product()
        quantity = 5

        self.__service.add_product_to_cart(product.id, quantity)

        product_into_cart = self.__cart_adapter.get_product(product.id)
        self.assertEqual(quantity, product_into_cart.quantity)

    def test_update_quantity_if_product_is_already_in_the_cart(self):
        product = self.__create_product()
        self.__service.add_product_to_cart(product.id, quantity=5)

        self.__service.add_product_to_cart(product.id, quantity=1)

        expected_quantity = 6
        product_into_cart = self.__cart_adapter.get_product(product.id)
        self.assertEqual(expected_quantity, product_into_cart.quantity)

    def test_throw_error_if_product_does_not_have_sufficient_stock(self):
        stock = 1
        product_without_stock = self.__create_product(stock=stock)

        with self.assertRaises(OutOfStockError) as context:
            self.__service.add_product_to_cart(product_without_stock.id, quantity=stock+1)

        expected_error_message = f"Out of stock for product #{product_without_stock.id}"
        self.assertEqual(expected_error_message, context.exception.description)

    def __create_product(self, stock: int = 300) -> Product:
        return self.__product_repo.create(
            name='book',
            author='me',
            picture='img.jpg',
            description='a cool book',
            category='other',
            stock=stock,
            likes=5,
            price=300
        )
