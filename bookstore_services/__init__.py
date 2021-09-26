__version__ = '0.1.0'

from flask import Flask, jsonify, make_response
from bookstore_services.modules.books.book_services import get_books_from_json_file

app = Flask(__name__)


@app.route('/books', methods=['GET'])
def books():
    resp = make_response(jsonify(get_books_from_json_file()))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
