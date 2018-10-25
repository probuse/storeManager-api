"""
    This module will contain tests for the Product class
"""
from unittest import TestCase
from app.models.product import Product

class ProductTestCase(TestCase):

    def setUp(self):
        "Initialize variables"
        self.product = Product(
            product_name = "Sugar", 
            product_price = 2000,
        )
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

    def test_three_product_object_created_successfully(self):
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
    
    def test_product_name_can_not_be_empty(self):
        "Test product name is a valid name"
        product = Product(
            product_name = "", 
            product_price = 3000
        )
        self.assertEqual("Product Name can not be empty", product.product_name)

    def test_product_name_can_not_be_a_character(self):
        "Test product name is a valid name"
        product = Product(
            product_name = "#!$@", 
            product_price = 3000
        )
        self.assertEqual(
            "Product Name must be contain atleast a letter or a digit", 
            product.product_name
        )

    def test_product_price_can_not_be_zero(self):
        "Test product price can not be zero"
        product = Product(
            product_name = "bread", 
            product_price = 0
        )
        self.assertEqual("Product Price can not be zero", product.product_price)

    def test_product_price_can_not_be_negative(self):
        "Test product price can not be a negative"
        product = Product(
            product_name = "bread", 
            product_price = -3000
        )
        self.assertEqual(
            "Product Price can not be a negative", 
            product.product_price
        )

    def test_product_price_can_not_be_a_string(self):
        "Product Price can not be a string"
        product = Product(
            product_name = "bread", 
            product_price = "thirty"
        )
        self.assertEqual(
            "Product Price can not be a string",
            product.product_price
        )

    def test_product_price_must_be_an_integer(self):
        "Test Product Price is integer"
        product = Product(
            product_name = "corn flakes", 
            product_price = 3.4
        )
        self.assertEqual(
            "Product Price must be an integer",
            product.product_price
        )

    def test_product_quantity_can_not_be_zero(self):
        "Test product quantity can not be zero"
        product = Product(
            product_name = "bread", 
            product_price = 2000, 
            product_quantity = 0
        )
        self.assertEqual(
            "Product Quantity can not be zero",
             product.product_quantity
        )

    def test_product_quantity_can_not_be_negative(self):
        "Test product quantity can not be a negative"
        product = Product(
            product_name ="bread", 
            product_price = 3000, 
            product_quantity = -23
        )
        self.assertEqual(
            "Product Quantity can not be a negative", 
            product.product_quantity
        )

    def test_product_quantity_can_not_be_a_string(self):
        "Product Quantity can not be a string"
        product = Product(
            product_name = "bread", 
            product_price = 1000, 
            product_quantity = "quantity"
        )
        self.assertEqual(
            "Product Quantity can not be a string",
            product.product_quantity
        )

    def test_product_quantity_must_be_an_integer(self):
        "Test Product Quantity is integer"
        product = Product(
            product_name = "corn flakes", 
            product_price = 32000, 
            product_quantity = 2.3
        )
        self.assertEqual(
            "Product Quantity must be an integer",
            product.product_quantity
        )

