import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 9000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'devkeykaffe'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'testkeykaffe'
