from bookstore.src.catalog import CatalogServices
from bookstore.src.shared.errors import NotFoundError
from bookstore.tests.test_cases.IntegrationTestCase import IntegrationTestCase


class ProductServicesTests(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self._service = CatalogServices.get_product_services()

    def test_create_product(self):
        product_data = {
            'name': 'book',
            'author': 'me',
            'description': 'a cool book',
            'picture': 'img.jpg',
            'category': 'other',
            'stock': 30,
            'likes': 5,
            'price': 300
        }

        product = self._service.create_product(**product_data)

        self.assertIsNotNone(product.id)
        self.assertEqual(product_data['name'], product.name)
        self.assertEqual(product_data['author'], product.author)
        self.assertEqual(product_data['description'], product.description)
        self.assertEqual(product_data['picture'], product.picture)
        self.assertEqual(product_data['category'], product.category)
        self.assertEqual(product_data['stock'], product.stock)
        self.assertEqual(product_data['likes'], product.likes)
        self.assertEqual(product_data['price'], product.price)
        self.assertEqual(f'R$ {int(product_data["price"]/100)},00', product.price_text.replace(u'\xa0', u' '))

    def test_get_product_list(self):
        product = self._service.create_product(**{
            'name': 'book',
            'author': 'me',
            'description': 'a cool book',
            'picture': 'img.jpg',
            'category': 'other',
            'stock': 30,
            'likes': 5,
            'price': 300
        })

        products = self._service.get_product_list()

        self.assertEqual(1, len(list(products)))
        self.assertEqual(product.id, products[0].id)

    def test_get_product(self):
        product_to_find = self._service.create_product(**{
            'name': 'book',
            'author': 'me',
            'description': 'a cool book',
            'picture': 'img.jpg',
            'category': 'other',
            'stock': 30,
            'likes': 5,
            'price': 300
        })

        product = self._service.get_product(product_to_find.id)

        self.assertEqual(product_to_find.id, product.id)

    def test_throw_not_found_error_if_product_does_not_exists(self):
        product_id = 100

        with self.assertRaises(NotFoundError) as context:
            self._service.get_product(product_id)

        expected_error_message = f"Product #{product_id} not found"
        self.assertEqual(expected_error_message, context.exception.description)
