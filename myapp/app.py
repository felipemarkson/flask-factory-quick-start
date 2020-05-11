from flask import Flask
# from extensions import myextension
from .blueprints import helloworld



def create_app():
    app = Flask(__name__)
    # myextension.init_app(app)
    app.register_blueprint(helloworld.bp)
    return app