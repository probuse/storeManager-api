"""
    contains tests for the Home View
"""
from tests.base_tests import BaseTestCase

class HomeViewTestCase(BaseTestCase):
    "TestCase for HomeView endpoint"

    def test_home_view_returns_200(self):
        "Test if home view responds with 200 status code"
        with self.client:
            response = self.get_home_view()
            self.assertEqual(response.status_code, 200)
            