from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False,unique=True)
    password = db.Column(db.String(20), nullable = False)


class Habit(db.Model,UserMixin)
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    timeStart = db.Column(db.Date,nullable=False)
    count = db.Column(db.Integer,default=0)
    