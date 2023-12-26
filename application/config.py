import os
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','C:\\Users\\baaqa\\OneDrive') # protects against forgery attacks , generated from "secrets"
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI','C:\\Users\\baaqa\\OneDrive')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL','C:\\Users\\baaqa\\OneDrive')
    MAIL_PASSWORD = os.getenv('PASS','C:\\Users\\baaqa\\OneDrive')
    # print(SECRET_KEY,SQLALCHEMY_DATABASE_URI,MAIL_PASSWORD,MAIL_USERNAME)