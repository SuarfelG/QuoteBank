from . import db
from flask_login import UserMixin

class Quotes(db.Model,UserMixin):
    __tablename__="Quote_Bank"

    id=db.Column(db.Integer , primary_key=True)
    Author=db.Column(db.String(50) ,nullable=False)
    Quote=db.Column(db.String(50) ,nullable=False)
