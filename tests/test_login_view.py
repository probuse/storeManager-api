"""
    Contains tests for the login view
"""
from tests.base_tests import BaseTestCase

class LoginTestCase(BaseTestCase):

    def setUp(self):
        "Initialize variables"
        super(LoginTestCase, self).setUp()
        self.store_attendant_login_data = dict(
            email="etwin@himself.com",
            password="12345678"
        )
        self.admin_login_data = dict(
            email="admin@gmail.com",
            password="iamadmin"
        )
    
    def test_store_attendant_post_request_to_login_returns_201_status_code(self):
        "Test post to login endpoint returns a success"
        with self.client:
            response = self.login_store_attendant_user(
                **self.store_attendant_login_data)
            self.assertEqual(response.status_code, 201)


    def test_store_attendant_logs_in_successfully(self):
        "Tests store attendant logins successfully"
        with self.client:
            response = self.login_store_attendant_user(
                **self.store_attendant_login_data)
            self.assertIn(
                b'{"message": "You are a store attendant"}', response.data)

    def test_admin_post_request_to_login_returns_201_status_code(self):
        "Test post to login endpoint returns a success"
        with self.client:
            response = self.login_admin_user(
                **self.store_attendant_login_data)
            self.assertEqual(response.status_code, 201)

    def test_admin_user_logs_in_successfully(self):
        "Tests admin logins successfully"
        with self.client:
            response = self.login_admin_user(**self.admin_login_data)
            self.assertIn(
                b'{"message": "You are admin"}', response.data)
