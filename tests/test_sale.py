"""
    Contains tests for the Sale class
"""
from unittest import TestCase
from app.models.sale import Sale

class SaleTestCase(TestCase):
    "TestCase for the Sale class"

    def test_sale_object_created_successfully(self):
        "Test sale project creation was successful"
        sale = Sale(
            product_id = 1, 
            products_sold = 2, 
            seller_id = 3
        )
        self.assertListEqual(
            [1, 2, 3],
            [sale.product_id, sale.products_sold, sale.seller_id]
        )

    def test_product_id_cannot_be_zero(self):
        "Test product id is not Zero"
        sale = Sale(
            product_id = 0,
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id can not be 0", sale.product_id)

    
    def test_product_id_must_be_greater_than_zero(self):
        "Test product id must be greater than zero"
        sale = Sale(
            product_id = -3,
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id must be greater than zero", sale.product_id)

    def test_product_id_cannot_be_a_string(self):
        "Test product id is not string"
        sale = Sale(
            product_id = 'etwin',
            products_sold = 2,
            seller_id = 1
        )
        self.assertEqual("Product id can not be a string", sale.product_id)

    def test_product_id_cannot_be_empty(self):
        "Test product id is not empty"
        sale = Sale(
            product_id = '',
            products_sold = 2,
            seller_id = 1
            )
        self.assertEqual("Product id can not be empty", sale.product_id)

    def test_products_sold_cannot_be_zero(self):
        "Test products sold can not be zero"
        sale = Sale(
            product_id = 2,
            products_sold = 0,
            seller_id = 1
        )
        self.assertEqual("Products sold can not be 0", sale.products_sold)

    def test_products_sold_cannot_be_an_empty_string(self):
        "Test products sold can not be empty string"
        sale = Sale(
            product_id = 4,
            products_sold = '',
            seller_id = 1
        )
        self.assertEqual(
            "Products sold can not be empty", sale.products_sold)

    def test_products_sold_cannot_be_a_string(self):
        "Test products sold can not be a string"
        sale = Sale(
            product_id = 4,
            products_sold = 'ten',
            seller_id = 1
        )
        self.assertEqual(
            "Products sold can not be a string", sale.products_sold)

    def test_products_sold_must_be_greater_than_zero(self):
        "Test products sold must be greater than zero"
        sale = Sale(
            product_id = 4,
            products_sold = -2,
            seller_id = 1
        )
        self.assertEqual(
            "Products sold must be greater than 0", sale.products_sold)

    def test_seller_id_cannot_be_zero(self):
        "Test seller_id is not zero"
        sale = Sale(
            product_id = 4,
            products_sold = 3,
            seller_id = 0
        ) 
        self.assertEqual(
            "Seller id can not be 0", sale.seller_id)

    def test_seller_id_must_be_greater_than_zero(self):
        "Test seller_id is greater than zero"
        sale = Sale(
            product_id = 4,
            products_sold = 3,
            seller_id = -3
        ) 
        self.assertEqual(
            "Seller id must be greater than 0", sale.seller_id)
