from flask import Flask
from flask_bootstrap import Bootstrap
from app.auth import auth 
from .config import Config
from models import UserModel

from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask("my_app")
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)