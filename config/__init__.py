import os

class Config(object):
    "Parent configuration class."
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URL = os.getenv('DATABASE_URL')


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
