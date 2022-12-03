from os import getenv, urandom

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from bookstore.database import close_database_session
from bookstore.routes import register_routes
from bookstore.middleware import register_middleware
from bookstore.commands import register_commands

# Variáveis de ambiente
load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = getenv('FLASK_SECRET_KEY', urandom(16))
    app.config['RESTX_VALIDATE'] = True

    # Banco de dados
    # Migrate(app, db)
    app.teardown_appcontext(close_database_session)

    # Rotas, middlwares e comandos
    register_routes(app)
    register_middleware(app)
    register_commands(app)

    return app