from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField
from wtforms.validators import DataRequired, Length, ValidationError, optional, EqualTo, ValidationError
from app import db
from models import User
from slugify import slugify
import re

def check_username(form,field): 
    if re.search('[^a-zA-Z0-9-]',field.data):
        raise ValidationError('əlavə simvol istifadə etmək olmaz')
    elif User.query.filter_by(username=field.data).first():
        raise ValidationError('Bu username istifade olunur')

def isEmail(form,field):
    if '@' not in field.data or '.' not in field.data:
        raise ValidationError('Duzgun mail yazin')
    elif User.query.filter_by(email=field.data).first():
        raise ValidationError('Bu email istifade olunub')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired('Bu xana doldurulmalidir'),Length(min=5,max=30),check_username])
    email = StringField('Email',validators=[DataRequired('Bu xana doldurulmalidir'),Length(min=5,max=50),isEmail])
    password = PasswordField('Parol',validators=[DataRequired('Bu xana doldurulmalidir'),\
        Length(min=8,max=30),EqualTo('confirm','parollar fərqlidi')])
    confirm = PasswordField('Parolun tekrari',validators=[DataRequired('Bu xana doldurulmalidir')])

class LoginForm(FlaskForm):
    EmailOrUsername = StringField('Username ve ya email',validators=[DataRequired()])
    password = PasswordField('Parol',validators=[DataRequired()])

class LinkForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    adress = StringField(validators=[DataRequired()])
    type = SelectField(choices=[('fb', 'Facebook'), ('wp', 'Whatsapp'), ('fbmsg', 'FB Messenger'),\
        ('ig', 'Instagram'),('ytb', 'Youtube'),('other', 'Other')])