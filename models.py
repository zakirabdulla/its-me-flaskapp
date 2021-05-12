from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

class CustomMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()


class User(UserMixin,CustomMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    links = db.relationship('Link', backref='user', lazy=True)
    socials = db.relationship('Social', backref='user', lazy=True)

    def __repr__(self):
        return self.username

    def __init__(self,password,*args,**kwargs):
        self.password = generate_password_hash(password)
        super(UserMixin,self).__init__(*args,**kwargs)

class Link(CustomMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(5),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    title = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'))

class Social(CustomMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    site = db.Column(db.String(5),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'))