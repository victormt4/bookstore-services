from os import getenv, urandom

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.routes import register_routes
from src.middleware import register_middleware
from src.commands import register_commands

# Variáveis de ambiente
load_dotenv()

# Flask
bookstore = Flask(__name__)
bookstore.secret_key = getenv('FLASK_SECRET_KEY', urandom(16))
bookstore.config['RESTX_VALIDATE'] = True

# Banco de dados
DATABASE_NAME = getenv('DATABASE_NAME', 'bookstore')
DATABASE_IP = getenv('DATABASE_IP', 'localhost')
DATABASE_USER = getenv('DATABASE_USER', 'postgres')
DATABASE_PASSWORD = getenv('DATABASE_PASSWORD', 'postgres')
bookstore.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP}:5432/{DATABASE_NAME}'
db = SQLAlchemy(bookstore)
Migrate(bookstore, db)

# Rotas, middlwares e comandos
register_routes(bookstore)
register_middleware(bookstore)
register_commands(bookstore)
