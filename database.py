from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import app
db=SQLAlchemy(app)
class user(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
