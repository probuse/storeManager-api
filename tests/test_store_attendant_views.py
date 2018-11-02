"""
    contains test for store attendant endpoint
"""
import json
from app import app
from db_helper import DBHelper
from tests.base_tests import BaseTestCase

class StoreAttendantTestCase(BaseTestCase):
    "TestCase for StoreAttendant endpoint"

    def setUp(self):
        "Initialize variables"
        super(StoreAttendantTestCase, self).setUp()
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

        self.store_attendant_data = dict(
            usernames="etwin himself",
            email="etwin@himself.com",
            phone_number=704800666,
            password="12345678"
        )

        self.admin_data = ('admin@gmail.com', 'admin', True)
    
    def tearDown(self):
        "drop database"
        self.db_helper.drop_database()

    def test_post_to_store_attendant_returns_201_status_code(self):
        "Tests if post request to store attendant returns 201"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            response = self.register_store_attendant(
                admin_token, **self.store_attendant_data)
            self.assertEqual(response.status_code, 201)

    def test_post_to_store_attendant_returns_success_message(self):
        "Tests post request to store attendant returns success message"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            response = self.register_store_attendant(
                admin_token, **self.store_attendant_data)
            resp = json.loads(response.data.decode())
            self.assertIn(
                "Store Attendant successfully added", 
                resp['message'])

    def test_get_all_store_attendants_returns_200_status_code(self):
        "Tests if get_store_attendants returns 200 status code"
        response = self.get_store_attendants()
        self.assertEqual(response.status_code, 200)

    def test_get_all_store_attendants_returns_no_store_attendants_added(self):
        "Tests if get_store_attendants returns no store attendants"
        response = self.get_store_attendants()
        resp = json.loads(response.data.decode())
        self.assertEqual(
            "No store attendants added yet", resp['message'])

    def test_get_all_store_attendants_returns_store_attendants_added(self):
        "Tests if get_store_attendants returns all store attendants"
        login_resp = self.login_admin_user(*self.admin_data)
        decoded_login_resp = json.loads(login_resp.data.decode())
        admin_token =  decoded_login_resp['token']

        self.register_store_attendant(
            admin_token, **self.store_attendant_data
        )
        response = self.get_store_attendants()
        resp = json.loads(response.data.decode())
        usernames = resp['result'][0]['usernames']
        email = resp['result'][0]['email']
        self.assertListEqual(
            ["etwin himself", "etwin@himself.com"],
            [usernames, email]
        )
    

