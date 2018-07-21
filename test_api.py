import unittest
import os
import json
from flask import Flask
from app.app import create_app
from instances.resource import entries_collection, EntryList


class EntryTestCase(unittest.TestCase):

    def setUp(self):
        """Set up method to run before each test cases.
        and defines the test variables and inizializes the app
        """

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.data = {"description": "Blockchain", "date": "01/01/18"}
        '''-----------testing code 200-----------'''


    def test_200_if_the_api_get_requests_works_as_expected(self):
        response = self.client.post(
            '/mydiary/api/v1.0/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        response = self.client.get('/mydiary/api/v1.0/user/entries')
        self.assertEqual(response.status_code, 200)


    def test_400_for_post_request(self):
        """Test bad request on post method"""
        empty = self.client.post(
            '/mydiary/api/v1.0/user/entries', data={}, content_type="application/json")
        self.assertEqual(empty.status_code, 400)
