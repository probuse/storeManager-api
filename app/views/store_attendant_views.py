"""
    contains views for store attendant endpoint
"""
from flask_restful import Resource, reqparse
from app.models.user import User

store_attendant_obj = User()

class StoreAttendantEndpoint(Resource):
    "Handles requests to /store-attendant endpoint"

    def get(self):
        "returns a list of all registered store attendants"
        return store_attendant_obj.get_store_attendants()