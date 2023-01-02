from sqlalchemy_utils.functions import database_exists, create_database, drop_database
from alembic import command

from bookstore.database import get_database_session, get_migration_object
from bookstore.tests.test_cases.ApplicationTestCase import ApplicationTestCase


class IntegrationTestCase(ApplicationTestCase):
    def setUp(self) -> None:
        super().setUp()
        self._create_database()
        self.db_connection = get_database_session()
        self.db_connection.begin()

    def tearDown(self) -> None:
        self.db_connection.rollback()
        self._drop_database()
        super().tearDown()

    def _create_database(self):
        if not database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')):
            create_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))
            self._run_migrations()

    def _drop_database(self):
        if database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')) and not self.app.config.get('REUSE_DB'):
            drop_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))

    def _run_migrations(self):
        migrations_path = self.app.config.get('MIGRATIONS_PATH')
        config = get_migration_object(self.app).get_config(directory=migrations_path)
        command.upgrade(config, 'head')
