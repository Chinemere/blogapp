from app import db
from flask_login import  UserMixin
from datetime import date

class Post(db.Model): 
    id = db.Column(db.Integer(), primary_key= True)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    comments = db.relationship('Comment', backref='post')
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    author = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    content = db.Column(db.Text())
    post_id= db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self) :
        return f'Comment "{self.content[:100]}"'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200),  nullable=False, unique=True)
    username = db.Column(db.String(200),  nullable=False, unique=True)
    password_hash = db.Column(db.Text,  nullable=False)
    post = db.relationship('Post', backref ="user") 

    def __repr__(self):
        return f'{self.username}'