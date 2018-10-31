"""
    Contains all the views for /sales endpoint
"""
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from app.models.sale import Sale

sales_obj = Sale()

class SingleSaleEndPoint(Resource):
    "Returns a single sale"
    def get(self, sale_id):
        'Returns a single sale with id of sale_id'
        return sales_obj.get_sale(sale_id)


class SaleEndPoint(Resource):
    "Handles all requests to /sales endpoint"

    def get(self):
        'Handles all get requests /sales'
        return sales_obj.get_sales()
        
    def post(self):
        'Handles all post requests to /sales endpoint'
        parser = reqparse.RequestParser()
        parser.add_argument(
            'product_name', 
            type=int, 
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
        return sales_obj.add_sale(**args)
        
