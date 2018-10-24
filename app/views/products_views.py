"""
    Contains all the Views for the /products endpoint
"""
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from app.models.product import Product

products = []

class SingleProductEndPoint(Resource):
    "Returns a single product"
    def get(self, product_id):
        'Returns a single product with id of product_id'
        for product in products:
            if product.product_id == int(product_id):
                response_data = dict(
                        product_id=product.product_id,
                        product_name=product.product_name,
                        product_price=product.product_price,
                        product_count=product.product_count
                    )
                return jsonify(response_data)
        return {
            'message': 'Product with id {} does not exist'.format(product_id)
        }
class ProductEndPoint(Resource):
    "Handles all requests to /products endpoint"
    def get(self):
        'Handles all get requests to /products endpoint'
        response_data = []
        if products:
            for product in products:
                data = dict(
                    product_id = product.product_id,
                    product_name = product.product_name,
                    product_price = product.product_price,
                    product_count = product.product_count
                )
                response_data.append(data)
            json_data = jsonify(response_data)
            return json_data
                
        return {'message': 'No Products added yet'}

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
