from json import load


def get_books_from_json_file() -> list:
    with open('bookstore_services/storage/books.json', 'r') as fp:
        return load(fp)
