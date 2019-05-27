'''Creating app'''

import os

from flask import Flask, redirect, jsonify
from flask_restful import Api
from flask_cors import CORS
from datetime import datetime, timedelta


from instance.config import app_config
from app.views.views import NewMessage
from app.utilities.db.connection import initializedb

"""importing the configurations from the .config file which is in the instance folder"""
def create_app(config_name):
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    """Catch all 400 related errors""" 
    @app.errorhandler(400)
    def bad_request_error(error):
        """400 error handler."""
        return jsonify({"error": "A bad request was sent to the server."}), 400

    """Catch all 404 errors"""
    @app.errorhandler(404)
    def not_found_error(error):
        """404 error handler."""
        return jsonify({"error": "Page not found, Check your URL and try again."}), 404

    """Catch all 500 errors"""
    @app.errorhandler(500)
    def internal_server_error(error):
        """500 error handler."""
        return jsonify({"error": "Internal server error has occured."}), 500

    # Initialize flask_restful and add routes
    api_endpoint = Api(app)

    # Meetups Resource v1
    api_endpoint.add_resource(NewMessage, '/api/v2/responses')

    # Add CORS to handle Access-Control-Allow-Origin issues
    CORS(app)

    initializedb()

    return app