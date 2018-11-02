"""
    Contains all the views for /sales endpoint
"""
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask_restful import Resource, Api, reqparse
from app.models.sale import Sale

sales_obj = Sale()

class SingleSaleEndPoint(Resource):
    "Returns a single sale"
    @jwt_required
    def get(self, sale_id):
        'Returns a single sale with id of sale_id'
        current_user = get_jwt_identity()
        is_admin = current_user['is_admin']
        if is_admin:
            return sales_obj.get_sale(sale_id)
        else:
            return {'message': 'Only admin access this endpoint'}, 403


class SaleEndPoint(Resource):
    "Handles all requests to /sales endpoint"
    @jwt_required
    def get(self):
        'Handles all get requests /sales'
        return sales_obj.get_sales()

    @jwt_required  
    def post(self):
        'Handles all post requests to /sales endpoint'
        parser = reqparse.RequestParser()
        parser.add_argument(
            'product_name', 
            type=str, 
            required=True,
            help="Product_name can not be empty" 
        )

        parser.add_argument(
            'products_sold', 
            type=int, 
            required=True,
            help="Products_sold can not be empty" 
        )

        parser.add_argument(
            'seller_id',
            type=int,
            required=True,
            help="seller_id can not be empty"
        )

        args = parser.parse_args()
        
        current_user = get_jwt_identity()
        is_admin = current_user['is_admin']
        if is_admin:
            return {'message': 'You are not allowed to make a sale'}, 403
        return sales_obj.add_sale(**args)
        
