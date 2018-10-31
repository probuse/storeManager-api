"""
    This module will contain the application
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['JWT_SECRET_KEY'] = '35cecd3c11bd54e46559a6e8bf20b5936a5764a1ec076b'
jwt = JWTManager(app)
from app.routes import ProductEndPoint, SingleProductEndPoint, SaleEndPoint, SingleSaleEndPoint 