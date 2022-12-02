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
DATABASE_URL_PADRAO = 'postgresql://postgres:postgres@db:5432/bookstore'
bookstore.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL', DATABASE_URL_PADRAO)
db = SQLAlchemy(bookstore)
Migrate(bookstore, db)

# Rotas, middlwares e comandos
register_routes(bookstore)
register_middleware(bookstore)
register_commands(bookstore)
