from .api.products_api import products_blueprint
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.register_blueprint(products_blueprint)
    return app

app = create_app()