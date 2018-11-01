"""
    Contains tests for the login view
"""
import json
from app import app
from db_helper import DBHelper
from tests.base_tests import BaseTestCase

class LoginTestCase(BaseTestCase):

    def setUp(self):
        "Initialize variables"
        super(LoginTestCase, self).setUp()
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        
        self.register_store_registration_data = dict(
            usernames="etwin himself",
            email="etwin@himself.com",
            is_admin=False,
            phone_number="704800666",
            password="12345678"
        )

        self.store_attendant_valid_login_data = dict(
            email="etwin@himself.com",
            password="12345678",
            is_admin=False
        )

        self.store_attendant_invalid_login_data = dict(
            email="cordelia@herself.com",
            password="iamcordelia",
            is_admin=False
        )

        self.admin_valid_login_data = dict(
            email="admin@gmail.com",
            password="admin",
            is_admin=True
        )

        self.admin_invalid_login_data = dict(
            email="notadmin@gmail.com",
            password="notadmin",
            is_admin=True
        )
    
        self.db_helper.delete_store_attendant_user(
            self.store_attendant_valid_login_data['email']
        )

    def test_store_attendant_post_request_to_login_returns_200_status_code(self):
        "Test post to login endpoint returns a success"
        with self.client:
            self.register_store_attendant(
                **self.register_store_registration_data
            )
            response = self.login_store_attendant_user(
                **self.store_attendant_valid_login_data)
            self.assertEqual(response.status_code, 200)


    def test_store_attendant_logs_in_successfully(self):
        "Tests store attendant logins successfully"
        with self.client:
            self.register_store_attendant(
                **self.register_store_registration_data
            )
            response = self.login_store_attendant_user(
                **self.store_attendant_valid_login_data)
            resp = json.loads(response.data)
            self.assertIn(
                "Logged in successfully as store attendant",
               resp['message'])

    def test_store_attendant_invalid_login_credentials_returns_401(self):
        "Tests store attendant fails to login in"
        with self.client:
            self.register_store_attendant(
                **self.register_store_registration_data
            )
            response = self.login_store_attendant_user(
                **self.store_attendant_invalid_login_data)
            self.assertEqual(response.status_code, 401)


    def test_store_attendant_invalid_login_credentials(self):
        "Tests store attendant fails to login in"
        with self.client:
            self.register_store_attendant(
                **self.register_store_registration_data
            )
            response = self.login_store_attendant_user(
                **self.store_attendant_invalid_login_data)
            resp = json.loads(response.data)
            self.assertIn(
                "Store attendant with email cordelia@herself.com does not exist",
                resp['message'])

    def test_admin_post_request_to_login_returns_200_status_code(self):
        "Test post to login endpoint returns a success"
        with self.client:
            response = self.login_admin_user(
                **self.admin_valid_login_data)
            self.assertEqual(response.status_code, 200)

    def test_admin_user_logs_in_successfully(self):
        "Tests admin logins successfully"
        with self.client:
            response = self.login_admin_user(
                **self.admin_valid_login_data)
            resp = json.loads(response.data)
            self.assertIn(
                'Logged in successfully as admin', 
                resp['message'])

    def test_admin_user_log_in_with_invalid_credentials_returns_404(self):
        "Tests admin login with invalid credentials"
        with self.client:
            response = self.login_admin_user(
                **self.admin_invalid_login_data)
            self.assertEqual(response.status_code, 401)

    def test_admin_user_log_in_with_invalid_credentials(self):
        "Tests admin login with invalid credentials"
        with self.client:
            response = self.login_admin_user(
                **self.admin_invalid_login_data)
            resp = json.loads(response.data)
            self.assertIn(
                "email notadmin@gmail.com does not belong to admin account",
                resp['message']
            )
