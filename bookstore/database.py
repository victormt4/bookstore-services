from flask import g, Flask
from os import getenv

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

DATABASE_NAME = getenv('DATABASE_NAME', 'bookstore')
DATABASE_IP = getenv('DATABASE_IP', 'localhost')
DATABASE_USER = getenv('DATABASE_USER', 'postgres')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', 'postgres')
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP}:5432/{DATABASE_NAME}'

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
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    database.init_app(app)
    Migrate(app, database, directory='bookstore/migrations')
    app.teardown_appcontext(close_database_session)