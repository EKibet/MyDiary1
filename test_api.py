import unittest
import os
import json
from flask import Flask, abort
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
    def test_if_post_adds_a_new_entry(self):
        """Test bad request on post method"""
        empty = self.client.post(
            '/mydiary/api/v1.0/user/entries', data={}, content_type="application/json")
        self.assertEqual(empty.status_code, 400)

    def test_api_post_method(self):
        """Test POST method"""
        response = self.client.post(
            '/mydiary/api/v1.0/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_api_get_specific_entry(self):
        """Test GET  method"""
        response = self.client.post(
            "/mydiary/api/v1.0/user/entries",
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response1 = self.client.get('/mydiary/api/v1.0/user/entries/1')
        self.assertEqual(response1.status_code, 200)
    def delete(self, contentID):
        del_entry = [
            del_entry for del_entry in entries_collection
            if del_entry["id"] == id
        ]
        if len(del_entry) == 0:
            abort(404)
        del entries_collection[0]
        return {"status": "Entry successfully deleted"}, 201
    def test_if_delete_an_entry_returns_expected_result(self):
        """Test Delete method"""
        response = self.client.post(
            '/mydiary/api/v1.0/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.delete('/mydiary/api/v1.0/user/entries/1')
        self.assertEqual(response.status_code, 201)
