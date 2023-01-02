from bookstore.src.catalog import Product
from bookstore.src.shared.repository import Repository
from bookstore.tests.test_cases.IntegrationTestCase import IntegrationTestCase


class RepositoryTests(IntegrationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self._entity_type = Product
        self._generic_repository = Repository[Product](self.db_connection, Product)

    def test_create(self):
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

        product = self._generic_repository.create(**product_data)

        self.assertIsInstance(product, self._entity_type)
        self.assertIsNotNone(product.id)
        self.assertEqual(product_data['name'], product.name)
        self.assertEqual(product_data['author'], product.author)
        self.assertEqual(product_data['description'], product.description)
        self.assertEqual(product_data['picture'], product.picture)
        self.assertEqual(product_data['category'], product.category)
        self.assertEqual(product_data['stock'], product.stock)
        self.assertEqual(product_data['likes'], product.likes)
        self.assertEqual(product_data['price'], product.price)

    def test_filter_by(self):
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
        product_data_to_ignore = product_data | {'name': 'other name'}
        product_to_find = self._generic_repository.create(**product_data)
        product_to_ignore = self._generic_repository.create(**product_data_to_ignore)

        product = self._generic_repository.filter_by(name=product_data['name'])

        self.assertEqual(1, len(list(product)))
        self.assertNotEqual(product_to_ignore.id, product[0].id)
        self.assertEqual(product_to_find.id, product[0].id)

    def test_get(self):
        product_to_find = self._generic_repository.create(**{
            'name': 'book',
            'author': 'me',
            'description': 'a cool book',
            'picture': 'img.jpg',
            'category': 'other',
            'stock': 30,
            'likes': 5,
            'price': 300
        })

        product = self._generic_repository.get(product_to_find.id)

        self.assertIsNotNone(product)
        self.assertEqual(product_to_find.id, product.id)
