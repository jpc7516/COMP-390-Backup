from app import db
from sqlalchemy.ext.declarative import declarative_base

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    image1 = db.Column(db.String, unique=True)
    image2 = db.Column(db.String, unique=True)
    vote1 = db.Column(db.Integer, unique=True)
    vote2 = db.Column(db.Integer, unique=True)
    
    def __init__(self, question, image1, image2):
        self.question = question
        self.image1 = image1
        self.image2 = image2
        self.vote1 = 0
        self.vote2 = 0
    
    def __repr__(self):
        return '<Post %r>' % (self.question)
        


    