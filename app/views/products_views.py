"""
    Contains all the Views for the /products endpoint
"""
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from app.models.product import Product

products = Product.products
product_obj = Product()

class SingleProductEndPoint(Resource):
    "Returns a single product"
    def get(self, product_id):
        'Returns a single product with id of product_id'
        response = product_obj.get_product(product_id)
        return response


class ProductEndPoint(Resource):
    "Handles all requests to /products endpoint"
    def get(self):
        'Handles all get requests to /products endpoint'
        response = product_obj.get_all_products()
        return response

    def post(self):
        'Handles all post requests to /products endpoint'
        parser = reqparse.RequestParser()
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
        response = product_obj.add_product(**args)

        return response
