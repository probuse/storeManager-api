"""
    Contains end point for home view
"""
from flask_restful import Resource

class HomeEndPoint(Resource):
    "Returns home view"

    def get(self):
        'Returns home view'
        return {"message": "Welcome to Store Manager API"}
