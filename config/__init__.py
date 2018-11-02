import os

class Config(object):
    "Parent configuration class."
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URL = 'postgres://bijzbcquzvtjyv:cfa4a3d9a8436ac6a0059cf1f776e24b5bd560f881ebe01237fbb8a6ea318646@ec2-54-204-14-96.compute-1.amazonaws.com:5432/dnm38gidg41rr'


class DevelopmentConfig(Config):
    "Configurations for Development environment"
    DEBUG = True

class TestingConfig(Config):
    "Configurations for Testing environment"
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/test_storemanager'

class ProductionConfig(Config):
    "Configurations for Production environment"
    DEBUG = False
    TESTING = False
