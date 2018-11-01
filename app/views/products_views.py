"""
    Contains all the Views for the /products endpoint
"""
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_restful import Resource, Api, reqparse
from app.models.product import Product

product_obj = Product()

class SingleProductEndPoint(Resource):
    "Returns a single product"
    def get(self, product_id):
        'Returns a single product with id of product_id'
        response = product_obj.get_product(product_id)
        return response
    
    def put(self, product_id):
        "modifies product with given product_id"
        parser = reqparse.RequestParser()
        parser.add_argument(
            'product_price',
            type=int,
            required=True,
            help="Product price can not be empty"
        )

        parser.add_argument(
            'product_quantity',
            type=int,
            required=True,
            help="Product quantity can not be empty"
        )
        args = parser.parse_args()
        return product_obj.modify_product(product_id, **args)

    @jwt_required
    def delete(self, product_id):
        "deletes product with a given product_id"
        current_user = get_jwt_identity()
        is_admin = current_user['is_admin']
        if is_admin:   
            return product_obj.delete_product(product_id)
        return {'message': 'Only admin can delete a product'}

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
        parser.add_argument(
            'product_quantity',
            type=int,
            required=True,
            help="Product quantity can not be empty"
        )
        args = parser.parse_args()
        response = product_obj.add_product(**args)

        return response
