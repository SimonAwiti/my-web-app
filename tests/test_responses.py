"""Unit tests for the meetups resources"""

import unittest
import json
from app import create_app


class TestResponse(unittest.TestCase):
    """Class containing all tests for the response resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client()
        self.response1 = {
            "name" : "Simon Awiti",
            "email" : "simon@bizztech.co.ke",
            "Phone" : "0722334455",
            "message" : "send me your resume/cv",
            }
        self.response2 = {
            "name" : "brian Awiti",
            "email" : "brian@bizztech.co.ke",
            "Phone" : "0722334455",
            "message" : "send me your resume/cv",
            }
        self.response3 = {
            "name" : "",
            "email" : "",
            "Phone" : "",
            "message" : "",
            }
        self.response4 = {
            "name" : "1",
            "email" : "1",
            "message" : "1",
            }

    def test_post_response(self):
        """Tests for posting a new response record"""
        response = self.client.post('/api/v1/responses',
                                    data=json.dumps(self.response1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Message succesfully send", str(response.data))

    def test_get_all_responses(self):
        """Test for getting all responses"""
        response = self.client.get('/api/v1/responses',
                                    data=json.dumps(self.response1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("All responses posted", str(response.data))

    def test_post_response_with_no_field(self):
        """Test for trying to post a response with no field"""
        response = self.client.post('/api/v1/responses',
                                    data=json.dumps(self.response3),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Kindly fill up all the fields", str(response.data))

    def test_post_response_with_digit_fields(self):
        """Test for trying to post a response with no field"""
        response = self.client.post('/api/v1/responses',
                                    data=json.dumps(self.response4
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("The fields should be described in words", str(response.data))
        