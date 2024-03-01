import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/temp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
