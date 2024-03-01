from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize bcrypt
bcrypt = Bcrypt()

# Initialize SQLAlchemy
db = SQLAlchemy()


class Admin(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    age = db.Column(db.Integer())

class KHR_Redddy(db.Model):
    insta_name = db.Column(db.String(100), primary_key=True)
    followers = db.Column(db.Integer())

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    