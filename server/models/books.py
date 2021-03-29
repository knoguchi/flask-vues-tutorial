from .base import db
import marshmallow as ma

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, nullable=False)


class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "title")

book_schema = BookSchema()
books_schema = BookSchema(many=True)