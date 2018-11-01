"""
    This module contains sales for the product object
"""
import json
from app import app
from db_helper import DBHelper
from tests.base_tests import BaseTestCase

class ProductTestCase(BaseTestCase):
    "TestCase to test ProductEndPoint"

    def setUp(self):
        "Initialize variables"
        super(ProductTestCase, self).setUp()
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

    def tearDown(self):
        "drop database"
        self.db_helper.drop_database()

    def test_add_product_returns_201_status_code(self):
        "Test adding product returns 201 status code"
        with self.client:
            response = self.add_product("egg", 500, 1)
            self.assertEqual(response.status_code, 201)

    def test_add_product_returns_message_to_user_with_created_product(self):
        "Test adding product returns information of added product"
        with self.client:
            self.add_product("egg", 500, 1)
            result = self.db_helper.get_a_product_from_db(1)
            product_name = result['product_name']
            product_price =result['product_price']
            product_quantity = result['product_quantity']
            self.assertListEqual(
                ["egg", 500, 1], 
                [product_name, product_price, product_quantity]
            )

    def test_get_products_returns_200_status_code(self):
        "Test product endpoint responds with a 200 status code"
        with self.client:
            response = self.get_products()
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_no_products_added_yet_if_no_products_are_added(self):
        "Test product endpoint returns No Products added yet when no products are added"
        with self.client:
            response = self.get_products()
            self.assertIn(b'No Products added yet', response.data)

    def test_get_a_product_returns_200_status_code(self):
        "Test /product/<product_product_name> endpoint responds with a 200 status code"
        with self.client:
            response = self.get_a_product(1)
            self.assertEqual(response.status_code, 200)

    def test_get_products_returns_no_product_if_product_name_doesnot_exist(self):
        "Test product endpoint returns Product does not exists"
        with self.client:
            self.add_product("egg", 500, 1)
            response = self.get_a_product(3)
            resp = json.loads(response.data.decode())
            self.assertEqual("Product with id 3 does not exist", resp['message'])

    def test_user_can_send_a_put_request_to_products_endpoint_successfully(self):
        "Tests user can successfully send put request"
        with self.client:
            self.add_product(1, 500, 1)
            response = self.modify_product(1, 3000, 3)
            self.assertEqual(response.status_code, 200)

    def test_user_can_successfully_modify_product(self):
        "Tests user can modify product successfully"
        with self.client:
            self.add_product("honey", 5000, 1)
            response = self.modify_product(1, 3200, 2)
            self.get_a_product(1)
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
    
    def test_user_can_not_modify_product_with_no_products_added(self):
        "Tests user can not modify a non existing product"
        with self.client:
            response = self.modify_product(1, 300, 2)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "No Products added yet", 
                decoded_response['message']
            )
            

    def test_user_cannot_delete_product_if_no_products_are_added_yet(self):
        "Tests user can only delete product if products have been added"
        with self.client:
            response = self.delete_product(1)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                "No Products added yet", 
                decoded_response['message']
            )

    def test_user_can_delete_product_if_it_exists(self):
        "Tests user can only delete product if it exists"
        with self.client:
            self.add_product("soda", 3000, 1)
            response = self.delete_product(1)
            decoded_response = json.loads(response.data.decode())
            self.assertEqual(
                "Product successfully deleted", 
                decoded_response['result']
            )

    def test_user_cannot_delete_product_which_does_not_exist(self):
        "Tests user can only delete product if it exists"
        with self.client:
            self.add_product("soda", 3000, 1)
            response = self.delete_product(3)
            decoded_response = json.loads(response.data.decode())
            self.assertIn(
                "Product with id 3 does not exist", 
                decoded_response['message']
            )
