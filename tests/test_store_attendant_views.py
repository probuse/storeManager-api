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
