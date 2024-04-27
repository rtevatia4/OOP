from flask import Flask
from .api.tickets_api import tickets_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tickets_blueprint)
    return app

app = create_app()