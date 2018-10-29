"""
    contains test for store attendant endpoint
"""
from tests.base_tests import BaseTestCase

class StoreAttendantTestCase(BaseTestCase):
    "TestCase for StoreAttendant endpoint"

    def setUp(self):
        "Initialize variables"
        super(StoreAttendantTestCase, self).setUp()
        self.store_attendant_data = dict(
            usernames="etwin himself",
            email="etwin@himself.com",
            phone_number=704800666,
            password="12345678"
        )

    def test_post_to_store_attendant_returns_200_status_code(self):
        "Tests if post request to store attendant returns 200"
        with self.client: 
            response = self.register_store_attendant(**self.store_attendant_data)
            self.assertEqual(response.status_code, 201)

    def test_post_to_store_attendant_returns_success_message(self):
        "Tests post request to store attendant returns success message"
        with self.client:
            response = self.register_store_attendant(**self.store_attendant_data)
            self.assertIn(
                b'{"message": "Store Attendant etwin himself with id 1 successfully added"}', 
                response.data)

    def test_get_all_store_attendants_returns_200_status_code(self):
        "Tests if get_store_attendants returns 200 status code"
        response = self.get_store_attendants()
        self.assertEqual(response.status_code, 200)

    def test_get_all_store_attendants_returns_no_store_attendants_added(self):
        "Tests if get_store_attendants returns no store attendants"
        response = self.get_store_attendants()
        self.assertIn(
            b'{"message": "No store attendants added yet"}', response.data)

    def test_get_all_store_attendants_returns_store_attendants_added(self):
        "Tests if get_store_attendants returns all store attendants"
        self.register_store_attendant(
            **self.store_attendant_data
        )
        response = self.get_store_attendants()
        self.assertIn(
            b'{"result": [{"user_id": 1, "usernames": "etwin himself", "email": "etwin@himself.com", "phone_number": "704800666", "password": "12345678"}]}',
             response.data)
    

