"""
    This module will contain the application
"""
import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__)

config_class = None
if os.getenv('CONFIG_CLASS') == "development":
    config_class = DevelopmentConfig
elif os.getenv('CONFIG_CLASS') == "testing":
    config_class = TestingConfig
elif os.getenv('CONFIG_CLASS') == 'deploy':
    config_class = ProductionConfig

app.config.from_object(config_class)
app.config['JWT_SECRET_KEY'] = '35cecd3c11bd54e46559a6e8bf20b5936a5764a1ec076b'
jwt = JWTManager(app)

from app.routes import ProductEndPoint, SingleProductEndPoint, SaleEndPoint, SingleSaleEndPoint 

@app.errorhandler(404)
def invalid_url(error):
    return jsonify({'message': "The url you entered does not exist on the system"}), 404

@app.errorhandler
def server_error(error):
    return jsonify({
        'message': "There is a problem with the server, try again"
        }, getattr(error, 'code', 500))

