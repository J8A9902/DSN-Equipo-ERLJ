from flask import Flask

from helpers.extensions import register_blueprints, initialize_database, setup_jwt

app: Flask = Flask(__name__)


with app.app_context():
    setup_jwt(app)
    initialize_database(app)
    register_blueprints(app)
