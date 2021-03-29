from flask import Flask
from flask_cors import CORS

from server.books import books_blueprint
from server.models import db, migrate, marshmallow


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # db
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    cors.init_app(app)

    # blueprint apps
    app.register_blueprint(books_blueprint, url_prefix='/api/books')

    # static files for dev

    return app
