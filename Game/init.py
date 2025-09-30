# Crafting Clicker Game - Initialization Module
# This module sets up the initial state of the game
# Imports
import os
import json
from Game.lib.settings import settings_menu
from Game.lib.templates import templates

# Initialize
def initialize_game():
    # Create necessary directories
    if not os.path.exists("Game/lib/settings"):
        os.makedirs("Game/lib/settings")
    if not os.path.exists("Game/lib/saves"):
        os.makedirs("Game/lib/saves")
    if not os.path.exists("Game/lib/assets"):
        os.makedirs("Game/lib/assets")

    # Check and create default settings file if it doesn't exist
    templates.Settings_Menu_Functions()
    settings_status = templates.Settings_Menu_Functions()
    if settings_status == "Does not exist":
        creation_status = settings_status.creation_status()
        if creation_status == "Created":
            print("Default settings file created.")
        else:
            print("Failed to create default settings file.")
    elif settings_status == "Exists":
        print("Settings file already exists.")
    else:
        print("Error checking settings file.")

    # Load settings
    with open("Game/lib/settings/settings.json", "r") as f:
        settings = json.load(f)
        print("Settings loaded:", settings)
    
    # Time to initialize the Main Menu
    