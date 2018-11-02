"""
    This module will contain tests for the sales endpoint
"""
import json
from app import app
from db_helper import DBHelper
from tests.base_tests import BaseTestCase
from app.models.sale import Sale

class SaleTestCase(BaseTestCase):
    "TestCase to test SaleEndPoint"

    def setUp(self):
        "Initialize variables"
        super(SaleTestCase, self).setUp()
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

        self.store_attendant_reg_data = dict(
            usernames="etwin himself",
            email="etwin@himself.com",
            phone_number="704800666",
            password="etwin"
        )

        self.admin_data = ('admin@gmail.com', 'admin', True)
        self.store_attendant_data = ('etwin@himself.com', 'etwin', False)

    def tearDown(self):
        "drop database"
        self.db_helper.drop_database()

    def test_add_sale_returns_201_status_code(self):
        "Test adding sale returns 201 status code"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 10, admin_token)
            response = self.add_sale("egg", 5, 1, attendant_token)
            self.assertEqual(response.status_code, 201)

    def test_add_sale_returns_message_to_user(self):
        "Test adding sale returns information of added sale"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 3, admin_token)
            sale_response = self.add_sale("egg", 2, 1, attendant_token)
            self.assertIn(b'2 egg(s) successfully sold', sale_response.data)

    def test_add_sale_if_product_name_doesnot_exist(self):
        "Test adding sale with invalid product_name"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 1, admin_token)
            sale_response = self.add_sale("bread", 2, 1, attendant_token)
            self.assertIn(b'Product with Product name bread does not exist', sale_response.data)

    def test_get_sales_returns_200_status_code(self):
        "Test a GET request to /sales returns a 200 status code"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            response = self.get_sales(admin_token)
            self.assertEqual(response.status_code, 200)

    def test_get_sales_when_no_sales_have_been_made(self):
        "Test request to /sales returns a message to user with no sales"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_sales(token)
            self.assertIn(b'No Sales made yet', response.data)

    def test_get_sales_when_sales_have_been_made_for_admin(self):
        "Test request to /sales returns a message to user with sales"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 3, admin_token)
            self.add_sale("egg", 2, 1, attendant_token)
            result = self.db_helper.get_sales_from_db()
            self.assertEqual(1, len(result))

    def test_get_sales_when_sales_have_been_made_for_store_attendant(self):
        "Test request to /sales returns a message to user with sales"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 3, admin_token)
            self.add_sale("egg", 2, 1, attendant_token)
            result = self.db_helper.get_sales_from_db()
            self.assertEqual(1, len(result))

    def test_get_a_sale_when_sale_does_not_exist_for_admin(self):
        "Tests response from get_a_sale with no sales made"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("egg", 500, 1, token)
            response = self.get_a_sale(1, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
              'No Sales made yet',
               decoded_response['message']
            )

    def test_get_a_sale_returns_sale(self):
        "Tests if get_a_sale returns when a sale is added"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 1, admin_token)
            response = self.add_sale("egg", 2, 1, attendant_token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                'Sale not possible Product egg has 1 product(s) left', 
                decoded_response['message'])

    def test_get_a_sale_returns_sale_does_not_exist_for_admin(self):
        "Tests if get_a_sale returns when a sale is added"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.register_store_attendant(
                admin_token, **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            attendant_token =  decoded_login_resp['token']

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            admin_token =  decoded_login_resp['token']

            self.add_product("egg", 500, 1, admin_token)
            response = self.add_sale('pk', 2, 1, attendant_token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                'Product with Product name pk does not exist', 
                decoded_response['message']
            )

    
