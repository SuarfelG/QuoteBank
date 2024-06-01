from . import db
from flask_login import UserMixin

class Quotes(db.Model,UserMixin):
    __tablename__="Quote_Bank"

    id=db.Column(db.Integer , primary_key=True)
    Author=db.Column(db.String(50) ,nullable=False)
    Quote=db.Column(db.String(50) ,nullable=False)


class Authentication(db.Model,UserMixin):
    __tablename__="Authentication"

    id=db.Column(db.Integer , primary_key=True)
    First_name=db.Column(db.String(50) ,nullable=False)
    Last_name=db.Column(db.String(50) ,nullable=False)
    Email=db.Column(db.String(50) ,nullable=False,unique=True)
    password=db.Column(db.String(50) ,nullable=False,unique=True)