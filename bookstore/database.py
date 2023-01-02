from os import getenv

from flask import g, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

metadata = MetaData()
database = SQLAlchemy(metadata=metadata)


def get_database_session() -> Session:
    if 'db' not in g:
        g.db = database.session
    return g.db


def close_database_session(e=None):
    db: Session | None = g.pop('db', None)

    if db is not None:
        db.close()


def config_database(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_credentials(app)
    database.init_app(app)
    migration = get_migration_object(app)
    app.teardown_appcontext(close_database_session)


def get_migration_object(app: Flask) -> Migrate:
    return Migrate(app, database, directory='bookstore/migrations')


def get_database_credentials(app: Flask) -> str:
    if app.config.get('TESTING'):
        TEST_DATABASE_NAME = getenv('DATABASE_NAME', 'bookstore_test')
        TEST_DATABASE_IP = getenv('DATABASE_IP', 'localhost')
        TEST_DATABASE_USER = getenv('DATABASE_USER', 'postgres')
        TEST_DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', 'postgres')
        TEST_DATABASE_URL = f'postgresql://{TEST_DATABASE_USER}:{TEST_DATABASE_PASSWORD}@{TEST_DATABASE_IP}:5432/{TEST_DATABASE_NAME}'
        return TEST_DATABASE_URL

    DATABASE_NAME = getenv('DATABASE_NAME', 'bookstore')
    DATABASE_IP = getenv('DATABASE_IP', 'localhost')
    DATABASE_USER = getenv('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', 'postgres')
    DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP}:5432/{DATABASE_NAME}'

    return DATABASE_URL
