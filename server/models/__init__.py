from .base import db, migrate, marshmallow
from .books import Book, book_schema, books_schema

__all__ = [
    db, migrate, marshmallow,
    Book, book_schema, books_schema
]
