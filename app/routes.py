"""
    Contain all api endpoints
"""
from flask_restful import Api
from app import app
from app.views.products_views import ProductEndPoint, SingleProductEndPoint
from app.views.sales_views import SaleEndPoint, SingleSaleEndPoint

api = Api(app)

# Endpoints to url mapping
api.add_resource(ProductEndPoint, '/api/v1/products')
api.add_resource(SingleProductEndPoint, '/api/v1/products/<product_id>')
api.add_resource(SaleEndPoint, '/api/v1/sales')
api.add_resource(SingleSaleEndPoint, '/api/v1/sales/<sale_id>')