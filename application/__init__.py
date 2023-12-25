# import necessary libraries
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '33754a16e180c8a45c1b1cdf867a2157' # protects against forgery attacks , generated from "secrets"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL','C:\\Users\\baaqa\\OneDrive')
app.config['MAIL_PASSWORD'] = os.getenv('PASS','C:\\Users\\baaqa\\OneDrive')
# print(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
mail = Mail(app)






from application import routes