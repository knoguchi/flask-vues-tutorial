import logging
from flask import Blueprint, request, jsonify
from flask_cors import CORS

from server.models import db, Book, book_schema, books_schema

log = logging.getLogger(__name__)
books_blueprint = Blueprint('books_blueprint', __name__)

CORS(books_blueprint)


@books_blueprint.route('/', methods=['GET', 'POST'])
def index():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        book = Book(
            id=post_data.get('id'),
            title=post_data.get('title'),
            status="new")
        log.info(book_schema.dump(Book))
        db.session.add(book)
        db.session.commit()
        response_object['message'] = 'Book added!'
    response_object['books'] = books_schema.dump(Book.query.all())
    return jsonify(response_object)

@books_blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        Book.query.filter_by(id=id).delete()
        db.session.commit()
        response_object['message'] = 'Book deleted!'
    response_object['books'] = books_schema.dump(Book.query.all())
    return jsonify(response_object)
