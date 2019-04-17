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

    def test_post_response(self):
        """Tests for posting a new response record"""
        response = self.client.post('/api/v1/responses',
                                    data=json.dumps(self.response1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Message succesfully send", str(response.data))