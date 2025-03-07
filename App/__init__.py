import os

from flask import Flask, render_template
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap



db = SQLAlchemy()
login_manager = LoginManager()


def create_app(test_config=None):


    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        

    login_manager.init_app(app)
    bootstrap = Bootstrap(app)
    db.init_app(app)

    
    #import models to initialize database
    from .models import User, Habit

    #Create tables
    with app.app_context():
        db.create_all()



    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import auth
    app.register_blueprint(auth.bp)

    from . import habits
    app.register_blueprint(habits.bp)


    @app.route('/')
    def index():
        return render_template('index.html')

    return app