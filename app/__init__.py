"""
    This module will contain the application
"""
import os
from flask import Flask
from config import DevelopmentConfig, TestingConfig

app = Flask(__name__)
config_class = None
if os.getenv('CONFIG_CLASS') == "development":
    config_class = DevelopmentConfig
elif os.getenv('CONFIG_CLASS') == "testing":
    config_class = TestingConfig
app.config.from_object(config_class)
from app.routes import ProductEndPoint, SingleProductEndPoint, SaleEndPoint, SingleSaleEndPoint 