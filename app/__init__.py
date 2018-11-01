"""
    This module will contain the application
"""
from flask import Flask
from config import DevelopmentConfig, TestingConfig

app = Flask(__name__)
config_class = ""

app.config.from_object(DevelopmentConfig)
print(app.config['DATABASE_URL'])
from app.routes import ProductEndPoint, SingleProductEndPoint, SaleEndPoint, SingleSaleEndPoint 