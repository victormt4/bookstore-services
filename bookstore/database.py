from flask import g
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, Session

DATABASE_NAME = getenv('DATABASE_NAME', 'bookstore')
DATABASE_IP = getenv('DATABASE_IP', 'localhost')
DATABASE_USER = getenv('DATABASE_USER', 'postgres')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', 'postgres')
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP}:5432/{DATABASE_NAME}'

engine = create_engine(DATABASE_URL)
metadata = MetaData()
scoped_session(sessionmaker(bind=engine))


def get_database_session() -> Session:
    if 'db' not in g:
        g.db = scoped_session(sessionmaker(bind=engine))
    return g.db


def close_database_session(e=None):
    db: scoped_session | None = g.pop('db', None)

    if db is not None:
        db.close()
