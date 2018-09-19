import os
import datetime


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@localhost/blog"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.urandom(24)
    REMEMBER_COOKIE_DURATION = datetime.timedelta(seconds=20)
