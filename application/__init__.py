# import necessary libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '33754a16e180c8a45c1b1cdf867a2157' # protects against forgery attacks , generated from "secrets"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from application import routes