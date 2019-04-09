"""app initializer """

import os

"""you import this to get all that we had defined and exported in the .env"""
from app import create_app
"""this is imported from the __init__.py file contained in the subdirectory called app"""
config_name = os.getenv("APP_SETTINGS")
"""Gets the app settings defined in the .env file"""
app = create_app(config_name)
"""defining the configuration to be used"""
if __name__ == '__main__':
app.run()