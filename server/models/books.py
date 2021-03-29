import marshmallow as ma

from .base import db


class Book(db.Model):
    # ISBN13
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, nullable=False)


class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "status")


book_schema = BookSchema()
books_schema = BookSchema(many=True)
