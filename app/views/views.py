"""Views for the Products Resource"""
from flask_restful import Resource, reqparse
from flask import request

from app.models.v2_models import Users
from app.utilities.validators import validate_responses

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', help="Kindly provide your name", required='True')
parser.add_argument('email', help="Kindly provide your email", required='True')
parser.add_argument('phone', help="Kindly provide your phone number", required='True')
parser.add_argument('message', help="Kindly provide a short message", required='True')


class NewMessage(Resource):
    """
    Class to handle adding and fetching all messages
    POST /api/v2/responses -> Creates a new response
    GET /api/v2/responses -> Gets all responses
    """
    def post(self):
        """Route to handle creating responses"""
        args = parser.parse_args()
        response = validate_responses(args)
        if response == "valid":
            return Users().send_message(
                args['name'],
                args['email'],
                args['phone'],
                args['message'])
        return response
    
    def get(self):
        """Route to fetch all response"""
        return Users().get_all_responses()
