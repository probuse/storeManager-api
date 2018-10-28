"""
    contains views for store attendant endpoint
"""
from flask_restful import Resource, reqparse
from app.models.user import User

store_attendant_obj = User()

class StoreAttendantEndPoint(Resource):
    "Handles requests to /store-attendant endpoint"

    def post(self):
        "handles post requests"
        parser = reqparse.RequestParser()
        parser.add_argument(
            'usernames',
            type=str,
            required=True,
            help="Store Attendant Names can not be empty"
        )
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help="Store Attendant email can not be empty"
        )
        parser.add_argument(
            'is_admin',
            type=bool,
            required=True,
            help="Store Attendant is_admin can not be empty"
        )
        parser.add_argument(
            'phone_number',
            type=str,
            required=True,
            help="Store Attendant Phone Number can not be empty"
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help="Store Attendant password can not be empty"
        )
        args = parser.parse_args()
        return store_attendant_obj.register_store_attendant(**args)
