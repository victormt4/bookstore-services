from os import getenv, urandom, path

from dotenv import load_dotenv

from flask import Flask

from bookstore.database import config_database
from bookstore.routes import register_routes
from bookstore.middleware import register_middleware
from bookstore.commands import register_commands

# Variáveis de ambiente
load_dotenv()


def create_app(config=None) -> Flask:
    app = Flask(__name__)
    app.secret_key = getenv('FLASK_SECRET_KEY', urandom(16))
    app.config['RESTX_VALIDATE'] = True
    app.config['MIGRATIONS_PATH'] = path.dirname(path.abspath(__file__)) + '/migrations'
    app.config['REUSE_DB'] = getenv('REUSE_DB', False)
    app.config.from_mapping(config)

    config_database(app)

    # Rotas, middlwares e comandos
    register_routes(app)
    register_middleware(app)
    register_commands(app)

    return app
