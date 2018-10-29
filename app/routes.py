"""
    Contain all api endpoints
"""
from flask_restful import Api
from app import app
from app.views.products_views import ProductEndPoint, SingleProductEndPoint
from app.views.sales_views import SaleEndPoint, SingleSaleEndPoint
from app.views.home_view import HomeEndPoint
from app.views.signup_view import SignupEndpoint
from app.views.store_attendant_views import StoreAttendantEndpoint

api = Api(app)

# Endpoints to url mapping
api.add_resource(HomeEndPoint, '/')
api.add_resource(ProductEndPoint, '/api/v1/products')
api.add_resource(SingleProductEndPoint, '/api/v1/products/<product_id>')
api.add_resource(SaleEndPoint, '/api/v1/sales')
api.add_resource(SingleSaleEndPoint, '/api/v1/sales/<sale_id>')
api.add_resource(SignupEndpoint, '/api/v1/auth/signup')
api.add_resource(StoreAttendantEndpoint, '/api/v1/store-attendants')
