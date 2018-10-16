"""
    This module will contain base tests for the api endpoints.
"""
from unittest import TestCase
from app import app

class BaseTestCase(TestCase):
    def setUp(self):
        "initialize up a client to for testing"
        self.client = app.test_client(self)

    def get_products(self):
        "returns response when the products endpoint hit"
        return self.client.get('/api/v1/products')