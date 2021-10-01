from typing import List


class Product:

    users_who_liked: List[str]
    stock: int
    category: str
    cover_picture: str
    description: str
    author: str
    name: str
    id: int

    def __init__(self, product_id: int, name: str, author: str, description: str, cover_picture: str, category: str, stock: int,
                 users_who_liked: List[str]):
        self.id = product_id
        self.name = name
        self.author = author
        self.description = description
        self.cover_picture = cover_picture
        self.category = category
        self.stock = stock
        self.users_who_liked = users_who_liked
