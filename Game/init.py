# Crafting Clicker Game - Initialization Module
# This module sets up the initial state of the game

import os
import json

# Initialize
def initialize_game():
    # Create necessary directories
    if not os.path.exists("Game/lib/settings"):
        os.makedirs("Game/lib/settings")
    if not os.path.exists("Game/lib/saves"):
        os.makedirs("Game/lib/saves")
    if not os.path.exists("Game/lib/assets"):
        os.makedirs("Game/lib/assets")

    # Create default settings file from settings_menu.template if it doesn't
    # exist
