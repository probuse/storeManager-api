"""
    contains views for store attendant endpoint
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user import User

store_attendant_obj = User()

class SignupEndpoint(Resource):
    "Handles requests to /signup endpoint"
    @jwt_required
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
        current_user = get_jwt_identity()
        is_admin = current_user['is_admin']
        if is_admin:
            return store_attendant_obj.register_store_attendant(**args)
        return {'message': 'Only admin can create a store attendant'}
