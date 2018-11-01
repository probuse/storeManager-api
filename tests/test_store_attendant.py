"""
    contains tests for store attendant object
"""
import json
from app import app
from db_helper import DBHelper
from unittest import TestCase
from app.models.user import User

class StoreAttendantTestCase(TestCase):

    def setUp(self):
        "Initialize variables"
        self.db_helper = DBHelper(app.config['DATABASE_URL'])
        self.db_helper.create_users_table()
        self.db_helper.create_products_table()
        self.db_helper.create_sales_table()

        self.store_attendant_obj = User(
            usernames = "etwin himself",
            email = "etwin@himself.com",
            phone_number = "704800666",
            password = "12345678"
        )

        self.store_attendant_data = dict(
            usernames="etwin himself",
            email="etwin@himself.com",
            phone_number="704800666",
            password="12345678"
        )

        # self.db_helper.delete_store_attendant_user(
        #     self.store_attendant_data['email']
        # )

    def tearDown(self):
        "drop database"
        self.db_helper.drop_database()
    
    def test_store_attendant_object_created_successfully(self):
        "Tests if store attendant object is created"
        self.assertListEqual(
            [None, "etwin himself", "etwin@himself.com", "704800666", "12345678"],
            [
                self.store_attendant_obj.user_id,
                self.store_attendant_obj.usernames,
                self.store_attendant_obj.email,
                self.store_attendant_obj.phone_number,
                self.store_attendant_obj.password
            ]
        )

    def test_get_store_attendant_id(self):
        "Tests if getter method works"
        self.assertEqual(None, self.store_attendant_obj.user_id)

    def test_set_user_id(self):
        "Tests if setter method works"
        self.store_attendant_obj.user_id = 1
        self.assertEqual(1, self.store_attendant_obj.user_id)

    def test_get_usernames(self):
        "Tests if getter method works"
        self.assertEqual(
            "etwin himself", self.store_attendant_obj.usernames)

    def test_set_usernames(self):
        "Tests if setter method works"
        self.store_attendant_obj.usernames = "alhazen"
        self.assertEqual(
            "alhazen", self.store_attendant_obj.usernames)

    def test_get_email(self):
        "Tests if getter method works"
        self.assertEqual("etwin@himself.com",
                         self.store_attendant_obj.email)

    def test_set_email(self):
        "Tests if setter method works"
        self.store_attendant_obj.email = "alhazen@vitrivuis.com"
        self.assertEqual("alhazen@vitrivuis.com",
                         self.store_attendant_obj.email)

    def test_get_phone_number(self):
        "Tests if getter method works"
        self.assertEqual(
            "704800666", self.store_attendant_obj.phone_number)

    def test_set_phone_number(self):
        "Tests if setter method works"
        self.store_attendant_obj.phone_number = "754640380"
        self.assertEqual("754640380",
                         self.store_attendant_obj.phone_number)
                        
    def test_get_password(self):
        "Tests if getter method works"
        self.assertEqual(
            "12345678", self.store_attendant_obj.password)

    def test_set_password(self):
        "Tests if setter method works"
        self.store_attendant_obj.password = "my-password"
        self.assertEqual("my-password",
                         self.store_attendant_obj.password)

    def test_store_attendants_list_initally_empty(self):
        "Tests if store attendants list is empty"
        self.assertListEqual([], self.store_attendant_obj.store_attendants)

    def test_store_attendants_list_has_attendant(self):
        "Tests if store attendant has attendant once attendant is added"
        self.store_attendant_obj.register_store_attendant(
            **self.store_attendant_data)
        store_attendants = self.store_attendant_obj.get_store_attendants()
        # result = json.loads(store_attendants.
        self.assertEqual(
            store_attendants['result'][0]['email'],
            'etwin@himself.com'
        )

