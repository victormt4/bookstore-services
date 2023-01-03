from bookstore.src.catalog import Product, CatalogServices
from bookstore.src.purchase.services.cart.cart_adapter import CartAdapter
from bookstore.src.purchase.services.cart.add_or_update_product_into_cart_service import AddOrUpdateProductIntoCartService
from bookstore.src.purchase.errors import OutOfStockError, NotFoundOnCartError
from bookstore.src.shared.repository import Repository
from bookstore.tests.test_cases.IntegrationTestCase import IntegrationTestCase


class AddOrUpdateProductIntoCartServiceTestCase(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self._product_repo = Repository[Product](self.db_connection, Product)
        self._cart_adapter = CartAdapter({})
        self._service = AddOrUpdateProductIntoCartService(
            self._cart_adapter,
            CatalogServices.get_product_services()
        )

    def _create_product(self, stock: int = 300) -> Product:
        return self._product_repo.create(
            name='book',
            author='me',
            picture='img.jpg',
            description='a cool book',
            category='other',
            stock=stock,
            likes=5,
            price=300
        )


class AddProductToCartTests(AddOrUpdateProductIntoCartServiceTestCase):
    def test_add_product_to_cart(self):
        product = self._create_product()
        quantity = 5

        self._service.add_product_to_cart(product.id, quantity)

        product_into_cart = self._cart_adapter.get_product(product.id)
        self.assertEqual(quantity, product_into_cart.quantity)

    def test_update_quantity_if_product_is_already_in_the_cart(self):
        product = self._create_product()
        self._service.add_product_to_cart(product.id, quantity=5)

        self._service.add_product_to_cart(product.id, quantity=1)

        expected_quantity = 6
        product_into_cart = self._cart_adapter.get_product(product.id)
        self.assertEqual(expected_quantity, product_into_cart.quantity)

    def test_throw_error_if_product_does_not_have_sufficient_stock(self):
        stock = 1
        product_without_stock = self._create_product(stock=stock)

        with self.assertRaises(OutOfStockError) as context:
            self._service.add_product_to_cart(product_without_stock.id, quantity=stock+1)

        expected_error_message = f"Out of stock for product #{product_without_stock.id}"
        self.assertEqual(expected_error_message, context.exception.description)


class UpdateProductQuantityTests(AddOrUpdateProductIntoCartServiceTestCase):
    def test_update_product_quantity(self):
        product = self._create_product()
        self._service.add_product_to_cart(product.id, quantity=5)

        self._service.update_product_quantity(product.id, quantity=3)

        expected_quantity = 8
        product_into_cart = self._cart_adapter.get_product(product.id)
        self.assertEqual(expected_quantity, product_into_cart.quantity)

    def test_remove_product_from_cart_if_new_quantity_is_zero(self):
        product = self._create_product()
        self._service.add_product_to_cart(product.id, quantity=5)

        self._service.update_product_quantity(product.id, quantity=0)

        self.assertIsNone(self._cart_adapter.get_product(product.id))

    def test_throw_error_if_new_quantity_is_greater_than_product_stock(self):
        stock = 20
        product_with_limited_stock = self._create_product(stock=stock)
        self._service.add_product_to_cart(product_with_limited_stock.id, quantity=stock)

        with self.assertRaises(OutOfStockError) as context:
            self._service.update_product_quantity(product_with_limited_stock.id, quantity=1)

        expected_error_message = f"Out of stock for product #{product_with_limited_stock.id}"
        self.assertEqual(expected_error_message, context.exception.description)

    def test_throw_error_if_product_is_not_in_the_cart(self):
        product = self._create_product()

        with self.assertRaises(NotFoundOnCartError) as context:
            self._service.update_product_quantity(product.id, quantity=1)

        expected_error_message = f"Product #{product.id} not found in cart"
        self.assertEqual(expected_error_message, context.exception.description)
