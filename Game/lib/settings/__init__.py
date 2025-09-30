# __init__ file for settings module
# This file makes the settings module a package.
# It can be used to initialize the package or set up any necessary imports.
import os
from . import settings
def SETTINGS_FILE():
    return os.path.join(os.path.dirname(__file__), 'settings.json')

# Sets settings.json to be able to be imported by a .py file
# in the any other directory in the project.
# Example usage:
# import os
# import json
# SETTINGS_FILE = os.path.join(os.path.dirname(__file__), 'settings.json')

# def load_settings():
#    if not os.path.exists(SETTINGS_FILE):
#        return {}
#    with open(SETTINGS_FILE, 'r') as file:
#        return json.load(file)

# def save_settings(settings):
#    with open(SETTINGS_FILE, 'w') as file:
#        json.dump(settings, file, indent=4)
