from flask_login import UserMixin
from . import db

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False,unique=True)
    password = db.Column(db.String(20), nullable = False)


class Habit(db.Model):

    __tablename__ = 'habits'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    count = db.Column(db.Integer,default=0)
    category = db.Column(db.String, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))





    