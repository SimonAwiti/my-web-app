import re
from datetime import datetime


def validate_responses(args):
    """validate response details"""
    try:
        if args["name"] == '' or args["name"].isspace() or \
           args["email"] == '' or args["email"].isspace() or \
           args["phone"] == '' or args["phone"].isspace() or \
           args["message"] == '' or args["message"].isspace() :
            return{
                "status": 401,
                "error": "Kindly note that the fields cannot be left empty"
                }, 401
        elif( args["name"].isdigit()) or ( args["email"].isdigit()) or ( args["message"].isdigit()) :
            return{
                "status": 401,
                "error": "The fields should be described in words"
                }, 401
        return"valid"
    except Exception as error:
        return{
                    "status": 401,
                    "error": "please provide all the fields, missing " + str(error)
                    }, 401
