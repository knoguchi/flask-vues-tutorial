from flask import Blueprint, request, jsonify
from flask_cors import CORS

from server.models import db, Book, book_schema, books_schema

books_blueprint = Blueprint('books_blueprint', __name__)

CORS(books_blueprint)


@books_blueprint.route('/', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        book = Book(id=123, title=post_data.get('title'), status="new")
        db.session.add(book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    response_object['books'] = books_schema.dump(Book.query.all())
    return jsonify(response_object)
