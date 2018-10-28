"""
    Contains all the Views for the /login endpoint
"""
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from app.models.user import User

user_obj = User()


class LoginEndPoint(Resource):
    "Handles all requests to /login endpoint"

    def post(self):
        'Handles all post requests to /login endpoint'
        parser = reqparse.RequestParser()
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help="email can not be empty"
        )
        parser.add_argument(
            'password',
            type=str,
            required=True,
            help="password can not be empty"
        )
        parser.add_argument(
            'is_admin',
            type=bool,
            required=True,
            help="is_admin can not be empty"
        )
        args = parser.parse_args()
        return user_obj.login_user(**args)

    
