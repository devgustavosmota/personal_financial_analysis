from flask import Flask
from .routes import register_blueprints

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile('config.py', silent=True)

    register_blueprints(app)

    return app
