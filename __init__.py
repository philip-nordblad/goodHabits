import os

from flask import Flask
import secrets
from SQLAlchemy import 


db = SQLAlchemy()
login_manager = LoginManager()

def create_app(test_config=None):


    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'


    login_manager.init_app(app)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app