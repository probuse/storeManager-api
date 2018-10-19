"""
This will contain all api endpoints
"""
import json
from flask import request
from flask_restful import Resource, Api, reqparse
from app import app
from app.models.product import Product

api = Api(app)
parser = reqparse.RequestParser()

products = []

class ProductEndPoint(Resource):
    "This resource will handle all requests to products endpoint"
    def get(self):
        'Handles all get requests to /products endpoint'
        return {'message': 'welcome to store Manager, Be patient as we set up {-: '}

    def post(self):
        'Handles all post requests to /products endpoint'
        parser.add_argument(
            'product_name', 
            type=str, 
            required=True,
            help="Product Name can not be empty" 
        )
        parser.add_argument(
            'product_price', 
            type=int, 
            required=True,
            help="Product Price can not be empty" 
        )
        args = parser.parse_args()
        product_name = args['product_name']
        product_price = args['product_price']

        if products:
            for product in products:
                if product.product_name == product_name:
                    return {
                        'message' : 'Product {} already exists'.format(product_name)
                    }

        product_id = len(products) + 1
        new_product = Product(
            product_name = product_name,
            product_price = product_price
        )
        new_product.product_id = product_id
        products.append(new_product)

        return {
            'message': 'Product {} with id {} successfully added'.format(
                product_name, product_id),
            }, 201

api.add_resource(ProductEndPoint, '/api/v1/products')
