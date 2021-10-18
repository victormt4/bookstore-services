__version__ = '0.1.0'

from os import getenv, urandom

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.routes import register_routes
from src.middleware import register_middleware

# Carregando variáveis de ambiente
load_dotenv()

# Configurando flask
app = Flask(__name__)
app.secret_key = getenv('FLASK_SECRET_KEY', urandom(16))
app.config['RESTX_VALIDATE'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('FLASK_DATABASE_URL')

# Configurando objetos do banco e migração
db = SQLAlchemy(app)
Migrate(app, db)

# Registrando rotas e middlewares
register_routes(app)
register_middleware(app)
