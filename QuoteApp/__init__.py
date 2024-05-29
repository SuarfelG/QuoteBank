from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def createApp():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="kindlypaycashonfriendlygoodservice"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///quote.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)

    from .models import Quotes
    create_database(app) 

    from .view import view
    from .QuoteManager import quote

    app.register_blueprint(quote , url_prefix='/')
    app.register_blueprint(view , url_prefix='/')

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print("Created database!")