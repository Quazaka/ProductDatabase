import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 9000

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'devkeykaffe'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'testkeykaffe'
