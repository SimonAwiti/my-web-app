"""handles all operations for creating and fetching data relating to users"""
import psycopg2
from flask import request, jsonify, make_response, json
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash


from app.utilities.db import connection


class Helper():
    """Carries out common functions"""

    def check_if_user_exists(self, email):
        """
        Helper function to check if a user exists
        Returns a message if a user already exists
        """
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM users WHERE email = '{}'".format(email))
            connect.commit()
            email = cursor.fetchone()
            cursor.close()
            connect.close()
            if email:
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            return {'error' : '{}'.format(error)}, 401

class Users(Helper):
    """Class to handle users"""
    def send_message(self, name, email, phone, message):
        """Method to handle user creation"""
        name = request.json.get('name', None)
        email = request.json.get('email', None)
        phone = request.json.get('phone', None)
        message = request.json.get('message', None)

        # Check for empty inputs
        if name == '' or email == '' or phone == '' or message == '':
            return{
                "status": 401,
                "error": "Neither of the fields can be left empty"
                }, 401

        present = Helper.check_if_user_exists(self, email)
        if present:
            return{
                "status": 409,
                "error": "There is a user with the same email registered"
                }, 409

        try:
            add_user = "INSERT INTO \
                        users (name, email, phone, message) \
                        VALUES ('" + name +"', '" + email +"', '" + phone +"', '" + message +"' )"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_user)
            connect.commit()
            response = jsonify({'status': 201,
                                "msg":'Message sent succesfully'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem sending your message to the database'})
            response.status_code = 500
            return response

    def get_all_responses(self):
        """Method to get all responses"""
        connect = connection.dbconnection()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return make_response(jsonify({
                "status": 200,
                "msg": "All sent messages",
                "data": [users]
                }))

    