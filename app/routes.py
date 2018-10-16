"""
This will contain all api endpoints
"""
from app import app
from flask_restful import Resource, Api

api = Api(app)

class Product(Resource):
    "This resource will handle all requests to products endpoint"
    def get(self):
        return {'message': 'welcome to store Manager, Be patient as we set up {-: '}
api.add_resource(Product, '/api/v1/products')
