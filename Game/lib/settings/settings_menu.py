# Settings Menu
# This file contains the settings menu for the game.
# It allows the player to adjust various settings such as sound volume, graphics
# quality, and control preferences.
# The settings are saved to a configuration file and loaded when the game
# starts.
# The settings menu is accessible from the main menu and can be navigated using
# the mouse or keyboard.
# The settings can be found in the 'settings.config' file in the same directory
# as this script.

import pygame
import os
import configparser
# Import settings from settings.config
# If settings.config does not exist, create it with default settings
if not os.path.exists("settings.config"):
    with open("settings.config", "w") as f:
        f.write("sound_volume=50\n")
        f.write("graphics_quality=Medium\n")
        f.write("control_scheme=Keyboard\n")
        f.write("fullscreen=False\n")
