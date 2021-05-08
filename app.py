from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@127.0.0.1:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdfkhsdflknsdfnsdflsidflmkdfgd'

from controllers import *
from models import *


if __name__ == "__main__":
    app.run(debug=True)