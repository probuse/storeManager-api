"""
    contains implementation for StoreAttendant class
"""

class User:

    store_attendants = []
    
    def __init__(self, **kwargs):
        self.user_id = None
        self.usernames = kwargs.get('usernames', None)
        self.email = kwargs.get('email', None)
        self.is_admin = kwargs.get('is_admin', False)
        self.phone_number = kwargs.get('phone_number', None)
        self.password = kwargs.get('password')
    
    def register_store_attendant(self, **data):
        "adds store attendant"
        usernames = data.get('usernames')
        email = data.get('email')
        phone_number = data.get('phone_number')
        password = data.get('password')

        user_id = len(User.store_attendants) + 1
        store_attendants = User.store_attendants

        if store_attendants:
            for attendant in store_attendants:
                if attendant.email == email:
                    return {
                        'message': 'Store Attendentant with email {} already exists'.format(
                            email
                        )
                    }
                elif attendant.user_id == user_id:
                    store_attendant_id += 1
        store_attendant = User(
            usernames=usernames,
            email=email,
            phone_number=phone_number,
            password=password
        )
        store_attendant.user_id = user_id
        store_attendants.append(store_attendant)
        return {
            'message': 'Store Attendant {} with id {} successfully added'.format(
                usernames, user_id),
        }, 201

    def login_user(self, **data):
        "logs in user"
        email = data.get('email')
        password = data.get('password')
        is_admin = data.get('is_admin')

        user_id = len(User.store_attendants) + 1
        store_attendants = User.store_attendants

        if is_admin:
            if email == "admin@gmail.com" and password == "admin":
                return {'message': 'we are logging you in as admin'}, 200
            return {'message': 'email {} does not belong to admin account'}, 401
            
        for attendant in store_attendants:
            if attendant.email == email and attendant.password == password:
                return {'message': 'You are a registered store attendant'}, 200
        return {'message': 'User with email {} does not exist'.format(email)}, 401

