from flask import Flask

from helpers.extensions import register_blueprints, initialize_database


app: Flask = Flask(__name__)


with app.app_context():
    initialize_database(app)
    register_blueprints(app)
