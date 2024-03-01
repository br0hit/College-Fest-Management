from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    age = db.Column(db.Integer())

class KHR_Redddy(db.Model):
    insta_name = db.Column(db.String(100), primary_key=True)
    followers = db.Column(db.Integer())

class User(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)