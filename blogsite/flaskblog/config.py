import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY');
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI');                  '''stores the site.db database at the current working directory'''
    MAIL_SERVER = os.environ.get('MAIL_SERVER'); 
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('BLOGIN_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('BLOGIN_EMAIL_PASS')

