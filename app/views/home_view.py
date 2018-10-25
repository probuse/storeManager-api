"""
    Contains end point for home view
"""
from flask_restful import Resource

class HomeEndPoint(Resource):
    "Returns home view"

    def get(self):
        'Returns home view'
        return {
            "message": "Welcome to Store Manager API",
            "active endpoints": {
                'products' : "https://storemanager-p-api.herokuapp.com/api/v1/products",
                'sales': "https://storemanager-p-api.herokuapp.com/api/v1/sales"
                }
            }
