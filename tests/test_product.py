"""
    This module will contain tests for the Product class
"""
import json
from app import app
from db_helper import DBHelper

from unittest import TestCase
from app.models.product import Product

class ProductTestCase(TestCase):

    def setUp(self):
        "Initialize variables"
        self.db_helper = DBHelper(app.config['DATABASE_URL'])

        self.product = Product(
            product_name = "Sugar", 
            product_price = 2000,
            product_quantity = 1
        )
        self.product_obj = Product()
        self.product_data = dict(
            product_name="pk", product_price=300, product_quantity=1)

        self.db_helper.delete_a_product_from_db(
            self.product_data['product_name']
        )
        self.num_products = len(self.db_helper.get_products_from_db())

    def tearDown(self):
        "clear data"
        Product.products[:] = []

    def test_one_product_object_created_successfully(self):
        "Tests if one product can be added"
        self.assertListEqual(
            [None, "Sugar", 2000, 1], 
            [
                self.product.product_id, 
                self.product.product_name, 
                self.product.product_price, 
                self.product.product_quantity
            ]
        )

    def test_product_object_created_successfully(self):
        "Tests if 3 products can be added"
        product = Product(
            product_name = "Sugar", 
            product_price = 2000,
            product_quantity = 3
        )
        self.assertListEqual(
            [None, "Sugar", 2000, 3], 
            [
                product.product_id, 
                product.product_name, 
                product.product_price, 
                product.product_quantity
            ]
        )

    def test_product_id_is_returned(self):
        "Tests if a product id is returned"
        self.assertEqual(self.product.product_id, None)
    
    def test_product_price_is_returned(self):
        "Tests if product price is returned"
        self.assertEqual(self.product.product_price, 2000)

    def test_product_name_is_returned(self):
        "Tests if product name is returned"
        self.assertEqual(self.product.product_name, "Sugar")

    def test_product_quantity_is_returned(self):
        "Tests if product quantity is returned"
        self.assertEqual(self.product.product_quantity, 1)

    def test_product_id_is_set(self):
        "Tests if a product id is set"
        self.product.product_id = 1
        self.assertEqual(self.product.product_id, 1)

    def test_product_price_is_set(self):
        "Tests if product price is set"
        self.product.product_price = 32000
        self.assertEqual(self.product.product_price, 32000)

    def test_if_product_name_is_set(self):
        "Tests if product name is set"
        self.product.product_name = "Flour"
        self.assertEqual(self.product.product_name, "Flour")

    def test_product_quantity_is_set(self):
        "Test if product quantity is set"
        self.product.product_quantity = 23
        self.assertEqual(self.product.product_quantity, 23)

    def test_product_is_added_succesfully(self):
        "Tests if product is added successfully"
        result = self.product_obj.add_product(**self.product_data)
        self.assertEqual(
            'Product successfully added',
            result[0]['message']
        )

    def test_length_of_products_after_product_is_added_succesfully(self):
        "Tests length of products list after product is added successfully"
        self.product_obj.add_product(**self.product_data)
        products = self.db_helper.get_products_from_db()
        self.assertEqual(
            len(products),
            self.num_products + 1
        )

    def test_user_can_not_add_product_twice(self):
        "Tests products names are unique"
        self.product_obj.add_product(**self.product_data)
        result = self.product_obj.add_product(**self.product_data)
        self.assertIn(
            'Product Already Exists',
            result['message']
        )
    
    def test_get_all_products_returns_no_products_with_no_products_added(self):
        "Tests if get_all_products returns no products"
        self.db_helper.delete_all_products()
        result = self.product_obj.get_all_products()
        self.assertEqual(
            'No Products added yet',
            result['message']
        )

    def test_get_product_returns_no_product_with_no_product_added(self):
        "Tests if get_product returns no product"
        self.db_helper.delete_all_products()
        result = self.product_obj.get_product('soda')
        self.assertEqual(
            'No Products added yet',
            result['message']
        )

    def test_get_product_returns_message_when_product_name_does_not_exist(self):
        "Tests if get_product returns no product"
        self.product_obj.add_product(**self.product_data)
        result = self.product_obj.get_product("ovacado")
        self.assertEqual(
            'Product with name ovacado does not exist',
            result['message']
        )

    def test_get_product_returns_result_information_about_added_product(self):
        "Tests if get_product returns a product"
        self.product_obj.add_product(**self.product_data)
        self.product_obj.add_product(
            product_name='candle', product_price=100, product_quantity=1)
        result =  self.product_obj.get_product('candle')
        product_name = result['result']['product_name']
        product_price = result['result']['product_price']
        product_quantity = result['result']['product_quantity']
        self.assertListEqual(
            ['candle', 100, 1],
            [product_name, product_price, product_quantity]
        )

    def test_add_invalid_product_name(self):
        "Tests if an invalid product_name is entered"
        result = self.product_obj.add_product(
            product_name="", product_price=200, product_quantity=1)
        self.assertEqual(
            {'product_name': 'Product Name must be a string'}, result)

    def test_add_invalid_product_price(self):
        "Tests if an invalid product_name is entered"
        result = self.product_obj.add_product(
            product_name="sugar", product_price=0, product_quantity=1)
        self.assertEqual(
            {'product_price': 'Product Price can not be less than one'}, result)

    def test_add_invalid_product_price_and_invalid_product_name(self):
        "Tests if an invalid product_name and an invalid product_price is entered"
        result = self.product_obj.add_product(
            product_name="", product_price=0, product_quantity=1)
        self.assertEqual(
            {
                "product_price": "Product Price can not be less than one",
                "product_name": "Product Name must be a string"
            }, result)

    def test_user_cannot_modify_product_if_no_products_exist(self):
        "Tests user can only modify existing products"
        result = self.product_obj.modify_product(
            product_name="Sugar",
            product_price=3200,
            product_quantity=1
        )
        self.assertEqual(
            'Product with name Sugar does not exist',
            result['message']
        )

    def test_user_can_not_modify_product_with_invalid_product_id(self):
        "Tests user can not modify product whose id does not exist"
        self.product_obj.add_product(**self.product_data)
        result = self.product_obj.modify_product(
            product_id=2,
            product_name="magic",
            product_price=3200,
            product_quantity = 1
        )
        self.assertEqual(
            {'message': 'Product with name magic does not exist'},
            result
        )

    def test_user_can_modify_product_successfully(self):
        "Tests user can modify product successfully"
        self.product_obj.add_product(**self.product_data)
        result = self.product_obj.modify_product(
            product_name="pk",
            product_price=1000,
            product_quantity=1
        )
        self.assertEqual(
            {'result': 'Product successfully updated'},
            result
        )   

    def test_user_cannot_delete_product_if_no_products_exist(self):
        "Tests user can only delete existing products"
        result = self.product_obj.delete_product("soda")
        self.assertEqual(
            'Product with name soda does not exist',
            result['message']
        )

    def test_deleted_product_no_longer_exists_in_system(self):
        "Tests if delete product has been deleted from system"
        self.product_obj.add_product(**self.product_data)
        self.product_obj.add_product(
            product_name="omo", product_price=2300, product_quantity=1)
        self.product_obj.delete_product("omo")
        response = self.product_obj.get_product("omo")
        self.assertEqual(
            'Product with name omo does not exist', 
            response['message']
            )
