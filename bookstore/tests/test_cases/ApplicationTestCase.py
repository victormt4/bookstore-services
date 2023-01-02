from unittest import TestCase

from bookstore import create_app


class ApplicationTestCase(TestCase):
    def setUp(self) -> None:
        self.app = create_app({'TESTING': True})
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self) -> None:
        self.context.pop()
