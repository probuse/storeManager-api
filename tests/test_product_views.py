"""
    This module contains sales for the product object
"""
import json
from app import app
from db_helper import DBHelper
from tests.base_tests import BaseTestCase
from app.models.user import User

class ProductTestCase(BaseTestCase):
    "TestCase to test ProductEndPoint"

    def setUp(self):
        "Initialize variables"
        super(ProductTestCase, self).setUp()
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

        self.admin_login_data = User(
            email='admin@gmail.com',
            password='admin',
            is_admin=True
        )

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

    def test_add_product_returns_201_status_code_for_admin(self):
        "Test adding product returns 201 status code"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.add_product("egg", 500, 1, token)
            self.assertEqual(response.status_code, 201)

    def test_add_product_returns_201_status_code_for_store_attendant(self):
        "Test adding product returns 201 status code"
        with self.client:
            self.register_store_attendant(
                **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.add_product("egg", 500, 1, token)
            self.assertEqual(response.status_code, 403)

    def test_add_product_not_allowed_for_store_attendant(self):
        "Test adding product returns information of added product"
        with self.client:
            self.register_store_attendant(
                **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.add_product("egg", 500, 1, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                'Only admin can add a product', 
                decoded_response['message']
            )

    def test_get_products_returns_200_status_code_for_admin(self):
        "Test product endpoint responds with a 200 status code"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_products(token)
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_200_status_code_for_store_attendants(self):
        "Test product endpoint responds with a 200 status code"
        with self.client:
            self.register_store_attendant(
                **self.store_attendant_reg_data
            )
            
            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_products(token)
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_no_products_added_yet_if_no_products_are_added_for_admin(self):
        "Test product endpoint returns No Products added yet when no products are added"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_products(token)
            self.assertIn(b'No Products added yet', response.data)

    def test_get_products_returns_no_products_added_yet_if_no_products_are_added_for_store_attendant(self):
        "Test product endpoint returns No Products added yet when no products are added"
        with self.client:
            self.register_store_attendant(
                **self.store_attendant_reg_data
            )

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_products(token)
            self.assertIn(b'No Products added yet', response.data)

    def test_get_a_product_returns_200_status_code(self):
        "Test /product/<product_product_name> endpoint responds with a 200 status code"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            response = self.get_a_product(1, token)
            self.assertEqual(response.status_code, 404)

    def test_get_products_returns_no_product_if_product_name_doesnot_exist_for_admin(self):
        "Test product endpoint returns Product does not exists"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("egg", 500, 1, token)
            response = self.get_a_product(3, token)
            resp = json.loads(response.data.decode())
            self.assertEqual("Product with id 3 does not exist", resp['message'])
        

    def test_admin_can_send_a_put_request_to_products_endpoint_successfully(self):
        "Tests admin can successfully send put request"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product(1, 500, 1, token)
            response = self.modify_product(1, 3000, 3, token)
            self.assertEqual(response.status_code, 200)

    def test_admin_can_successfully_modify_product(self):
        "Tests admin can modify product successfully"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("honey", 5000, 1, token)
            response = self.modify_product(1, 3200, 2, token)
            self.get_a_product(1, token)
            db_result = self.db_helper.get_a_product_from_db(1)

            product_name = db_result['product_name']
            product_price = db_result['product_price']
            product_quantity = db_result['product_quantity']
        
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "Product successfully updated", 
                decoded_response['result']
            )
            self.assertListEqual(
                ["honey", 3200, 2],
                [product_name, product_price, product_quantity]
            )

    def test_store_attendant_can_successfully_modify_product(self):
        "Tests store attendant can modify product successfully"
        with self.client:
            self.register_store_attendant(
                **self.store_attendant_reg_data
            )

            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("honey", 5000, 1, token)
            response = self.modify_product(1, 3200, 2, token)
            self.get_a_product(1, token)
            db_result = self.db_helper.get_a_product_from_db(1)

            product_name = db_result['product_name']
            product_price = db_result['product_price']
            product_quantity = db_result['product_quantity']
        
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "Product successfully updated", 
                decoded_response['result']
            )
            self.assertListEqual(
                ["honey", 3200, 2],
                [product_name, product_price, product_quantity]
            )
    
    def test_admin_can_not_modify_product_with_no_products_added(self):
        "Tests admin can not modify a non existing product"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']
            
            response = self.modify_product(1, 300, 2, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "No Products added yet", 
                decoded_response['message']
            )
            

    def test_user_cannot_delete_product_if_no_products_are_added_yet(self):
        "Tests user can only delete product if products have been added"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']
                        
            response = self.delete_product(1, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                "No Products added yet", 
                decoded_response['message']
            )

    def test_user_can_not_delete_with_no_authorization_header(self):
        "Tests user can only delete product if they are autenticated"
        with self.client:
            self.add_product("soda", 3000, 1, None)
            response = self.delete_product(1)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                'Missing Authorization Header', 
                decoded_response['msg']
            )

    def test_admin_user_can_delete_product_if_it_exists(self):
        "Tests admin can delete product"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']
            self.add_product("soda", 3000, 1, token)
            response = self.delete_product(1, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "Product successfully deleted", 
                decoded_response['result']
            )

    def test_store_attendant_user_can_not_delete_product(self):
        "Tests store attendant user can not delete product"
        with self.client:
            reg_response = self.register_store_attendant(
                **self.store_attendant_reg_data
            )
            decoded_reg_response = json.loads(reg_response.data.decode())

            login_resp = self.login_store_attendant_user(
                *self.store_attendant_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("soda", 3000, 1, token)
            response = self.delete_product(1, token)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "Store Attendant successfully added",
                decoded_reg_response['message']
            )
            self.assertEqual(
                "Only admin can delete a product", 
                decoded_response['message']
            )

    def test_admin_cannot_delete_product_which_does_not_exist(self):
        "Tests user can only delete product if it exists"
        with self.client:
            login_resp = self.login_admin_user(*self.admin_data)
            decoded_login_resp = json.loads(login_resp.data.decode())
            token =  decoded_login_resp['token']

            self.add_product("soda", 3000, 1, token)
            response = self.delete_product(3, token)
            decoded_response = json.loads(response.data.decode())
            self.assertIn(
                "Product with id 3 does not exist", 
                decoded_response['message']
            )
