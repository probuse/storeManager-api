"""
    This module will contain the application
"""
from flask import Flask

app = Flask(__name__)

from app.routes import ProductEndPoint, SingleProductEndPoint