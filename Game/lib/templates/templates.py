# Templates for the game
# This module provides functions to determine if template files exist, detect if
# the file that the templates are based on exists, and create default files from
# templates if they do not exist
import os
import json
from Game.lib.settings import settings_menu

# Check if a template file exists
def template_exists(template_path):
    return os.path.exists(template_path)
    
def Settings_Menu_Functions_Function_List():
    return {}
    
    
# Set the settings file path
def settings_file_path():
    return "Game/lib/settings"
# Settings menu Functions
# Check if the settings menu template exists
def Settings_Menu_Functions():
    def settings_menu_template_exists():
        # Add settings_menu_template_exists to the function list
        Settings_Menu_Functions_Function_List()["settings_menu_template_exists"] = settings_menu_template_exists
        # Check if the settings menu template exists
        if not template_exists("Game/lib/templates/settings_menu_template.template"):
            return False
        return True
    # Create default settings file from settings menu template
    def create_default_settings_data():
        # Add create_default_settings_data to the function list
        Settings_Menu_Functions_Function_List()["create_default_settings_data"] = create_default_settings_data
        if settings_menu_template_exists():
            def get_default_settings():
                # Add get_default_settings to the function list
                Settings_Menu_Functions_Function_List()["get_default_settings"] = get_default_settings
                # Get the template data
                with open("Game/lib/templates/settings_menu_template.template", "r") as file:
                    template_data = file.read()
                    return json.loads(template_data)
                return {}

    # Check if the settings file already exists
    def detect_settings_file():
        if not os.path.exists("Game/lib/settings/settings.json"):
            # If it doesn't exist return Does not exist
            if not detect_settings_file():
                create_default_settings_file()
            return "Does not exist"
        # Add detect_settings_file to the function list
        Settings_Menu_Functions_Function_List()["detect_settings_file"] = detect_settings_file
        # If it does exist return Exists
        return "Exists"
    
    # Create the default settings file if it doesn't exist
    def create_default_settings_file():
        # Get the default settings from the default settings data function
        default_settings = create_default_settings_data()
        # Create an empty .config file
        if not os.path.exists(settings_file_path()):
            os.makedirs(settings_file_path())
            with open(os.path.join(settings_file_path(), ".config"), "w") as file:
                # Write the default settings to the file
                json.dump(default_settings, file, indent=4)
                # Test if the file was created successfully
                if os.path.exists(os.path.join(settings_file_path(), ".config")):
                    return "Created"
                # If it fails retry creating the file
                create_default_settings_file()
                return "Failed"
        return "Exists"
    def rename_settings_file():
        # Add rename_settings_file to the function list
        Settings_Menu_Functions_Function_List()["rename_settings_file"] = rename_settings_file
        # Rename the file to settings.json
        os.rename(os.path.join(settings_file_path(), ".config"), os.path.join(settings_file_path(), "settings.json"))
        # Detect if the file was renamed successfully
        if not os.path.exists(os.path.join(settings_file_path(), "settings.config")):
            # If it fails retry renaming the file
            rename_settings_file()
            return "Failed"
        return "Renamed"
    # If it was renamed successfully return Created
    return "Created"
    # If the settings file already exists, do nothing

def Settings_Menu_Functions_Creation_Status():
    return Settings_Menu_Functions_Function_List().get("create_default_settings_file", lambda: "Function not found")()
def creation_status():
    return Settings_Menu_Functions_Creation_Status()
def Settings_Menu_Functions_Detect_Status():
    return Settings_Menu_Functions_Function_List().get("detect_settings_file", lambda: "Function not found")()
def detect_status():
    return Settings_Menu_Functions_Detect_Status()
def Settings_Menu_Functions_Rename_Status():
    return Settings_Menu_Functions_Function_List().get("rename_settings_file", lambda: "Function not found")()
def rename_status():
    return Settings_Menu_Functions_Rename_Status()
def Settings_Menu_Functions_Settings_Menu_Status():
    return Settings_Menu_Functions_Function_List().get("settings_menu", lambda: "Function not found")()
def settings_menu_status():
    return Settings_Menu_Functions_Settings_Menu_Status()
def Settings_Menu_Functions_Settings_Menu_Template_Exists_Status():
    return Settings_Menu_Functions_Function_List().get("settings_menu_template_exists", lambda: "Function not found")()
def settings_menu_template_exists_status():
    return Settings_Menu_Functions_Settings_Menu_Template_Exists_Status()
