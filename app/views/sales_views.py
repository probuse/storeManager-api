"""
    Contains all the views for /sales endpoint
"""
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from app.models.sale import Sale
from app.views.products_views import products as _products

products = _products
sales = []

class SingleSaleEndPoint(Resource):
    "Returns a single sale"
    def get(self, sale_id):
        'Returns a single sale with id of sale_id'
        for sale in sales:
            if sale.sale_id == int(sale_id):
                response_data = dict(
                        sale_id=sale.sale_id,
                        product_id=sale.product_id,
                        products_sold=sale.products_sold,
                        sale_date=sale.sale_date
                    )
                return jsonify(response_data)
        return {
            'message': 'Sale with id {} does not exist'.format(sale_id)
        }


class SaleEndPoint(Resource):
    "Handles all requests to /sales endpoint"

    def get(self):
        'Handles all get requests /sales'
        response_data = []
        if sales:
            for sale in sales:
                data = dict(
                    sale_id = sale.sale_id,
                    product_id = sale.product_id,
                    products_sold = sale.products_sold,
                    sale_date = sale.sale_date
                )
                response_data.append(data)
            return jsonify(response_data)
        return {'message': 'No Sales made yet'}
    
    def post(self):
        'Handles all post requests to /sales endpoint'
        parser = reqparse.RequestParser()
        parser.add_argument(
            'product_id', 
            type=int, 
            required=True,
            help="Product id can not be empty" 
        )

        parser.add_argument(
            'products_sold', 
            type=int, 
            required=True,
            help="Products sold can not be empty" 
        )

        args = parser.parse_args()
        product_id = args['product_id']
        products_sold = args['products_sold']

        if products:
            for product in products:
                if product.product_id == int(product_id):
                    sale = Sale(
                        product_id = product.product_id,
                        products_sold = products_sold 
                    )
                    sale.sale_id = len(sales) + 1
                    sales.append(sale)
                    return {
                        'message': '{} {}(s) successfully sold'.format(
                            products_sold, 
                            product.product_name
                            )
                    }
        return {
            'message': 'Product with Product id {} does not exist'.format(product_id)
            }
            