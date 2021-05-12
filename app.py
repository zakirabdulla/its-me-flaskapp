from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_qrcode import QRcode
app = Flask(__name__)

login_manager = LoginManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@127.0.0.1:3306/db'
app.config['SECRET_KEY'] = 'sdfkhsdflknsdfnsdflsidflmkdfgd'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
QRcode(app)

from controllers import *
from models import *


if __name__ == "__main__":
    app.run(debug=True)