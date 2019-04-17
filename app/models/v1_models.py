"""handles all operations dealing with responsess"""

from flask import request, jsonify
from datetime import datetime, timedelta
from uuid import uuid4


responses = []


class Helper():
    """Carries out common functions"""
    def responses(self, email):
        isresponse = [response for response in responses if response["email"] == email]
        if isresponse:
            return isresponse
        False


class Responses(Helper):
    """Class to handle the response operations """

    def add_resp(self, name, email, phone, message):
        name = request.json.get('name', None)
        email = request.json.get('email', None)
        phone = request.json.get('phone', None)
        message = request.json.get('message', None)

        present = Helper.responses(self, email)
        if present:
            return{
                "status": 401,
                "error": "You have already sent your response, consider using a different email"
                }, 401
           
        
        resp_dict={
            "meetup_id": len(responses) + 1,
            "sentOn" : str(datetime.now()),
            "name" : name,
            "email" : email,
            "phone" : phone,
            "message" : message
        }
        responses.append(resp_dict)
        return {
            "status": 201,
            "data": resp_dict,
            "Message": "Message succesfully send"
        }, 201
        