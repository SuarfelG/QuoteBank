from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_session import Session
from datetime import timedelta

db = SQLAlchemy()


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "1234567890"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:goat300@/quotesdb'
    app.config["SESSION_TYPE"]="sqlalchemy"
    app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(minutes=5)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    create_database(app)

    from .models import Authentication


    from .view import view
    from .QuoteManager import QuoteManager

    app.register_blueprint(QuoteManager, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')


    login_manager = LoginManager()
    login_manager.login_view = "view.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(first_name):
        return Authentication.query.get(first_name)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print("Created database!")





