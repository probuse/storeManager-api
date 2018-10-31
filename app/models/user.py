"""
    contains implementation for StoreAttendant class
"""
from db_helper import DBHelper
from app import app

from flask_jwt_extended import create_access_token

class User:

    store_attendants = []
    
    def __init__(self, **kwargs):
        self.user_id = None
        self.usernames = kwargs.get('usernames', None)
        self.email = kwargs.get('email', None)
        self.is_admin = kwargs.get('is_admin', False)
        self.phone_number = kwargs.get('phone_number', None)
        self.password = kwargs.get('password')

        self.db_helper = DBHelper(app.config['DATABASE_URL'])
    
    def register_store_attendant(self, **data):
        "adds store attendant"
        usernames = data.get('usernames')
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')

        store_attendant = User(
            usernames=usernames,
            email=email,
            phone_number=phone_number,
            is_admin=False,
            password=password
        )

        self.db_helper.add_user_to_db(store_attendant)

        return {
            'message': 'Store Attendant successfully added',
        }, 201

    def get_store_attendants(self):
        "returns all store attendants"
        store_attendants = self.db_helper.get_store_attendants_from_db()

        response_data = []
        if store_attendants:
            for attendant in store_attendants:
                data = dict(
                    user_id=attendant['user_id'],
                    usernames=attendant['usernames'],
                    email=attendant['email'],
                    phone_number=attendant['phone_number'],
                    password=attendant['password']
                )
                response_data.append(data)
            return {'result': response_data}

        return {'message': 'No store attendants added yet'}

    def login_user(self, **data):
        "logs in user"
        email = data.get('email')
        password = data.get('password')
        is_admin = data.get('is_admin')

        store_attendants = self.db_helper.get_store_attendants_from_db()

        if is_admin:
            if email == "admin@gmail.com" and password == "admin":
                admin = dict(
                    email=email,
                    is_admin=True
                )
                access_token = create_access_token(identity=admin)
                return {'message': 'Logged in successfully as admin', 'token': access_token}, 200
            return {'message': 'email {} does not belong to admin account'.format(email)}, 401

        for attendant in store_attendants:
            if attendant['email'] == email and attendant['password'] == password:
                admin = dict(
                    email=email,
                    is_admin=attendant.is_admin
                )
                access_token = create_access_token(identity=admin)
                return {'message': 'Logged in successfully as store attendant', 'token': access_token}, 200
        return {'message': 'Store attendant with email {} does not exist'.format(email)}, 401

