# Settings Menu Assets List
# This file contains the assets used in the settings menu.
# It includes images, fonts, and other resources needed for the settings menu
# UI.
import os
import pygame

# Define the path to the assets directory
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '../../assets/settings_menu')

# Load images
BUTTON_IMAGE = pygame.image.load(os.path.join(ASSETS_DIR, 'button.png')).convert_alpha()
SLIDER_IMAGE = pygame.image.load(os.path.join(ASSETS_DIR, 'slider.png')).convert_alpha()
DROPDOWN_IMAGE = pygame.image.load(os.path.join(ASSETS_DIR, 'dropdown.png')).convert_alpha()
CHECKBOX_IMAGE = pygame.image.load(os.path.join(ASSETS_DIR, 'checkbox.png')).convert_alpha()

# Load fonts
FONT = pygame.font.Font(os.path.join(ASSETS_DIR, 'font.ttf'), 24)

# Settings Menu Assets Class
class SettingsMenuAssets:
    def __init__(self):
        self.button_image = BUTTON_IMAGE
        self.slider_image = SLIDER_IMAGE
        self.dropdown_image = DROPDOWN_IMAGE
        self.checkbox_image = CHECKBOX_IMAGE
        self.font = FONT
        self.load_additional_assets()
    def load_additional_assets(self):
        # Load any additional assets here
        self.additional_image = pygame.image.load(os.path.join(ASSETS_DIR, 'additional.png')).convert_alpha()
        self.another_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'another_font.ttf'), 18)
        # Add more assets as needed
    def get_asset(self, asset_name):
        return getattr(self, asset_name, None)
# Example usage:
# assets = SettingsMenuAssets()
# button_image = assets.get_asset('button_image')
# slider_image = assets.get_asset('slider_image')
# dropdown_image = assets.get_asset('dropdown_image')
# checkbox_image = assets.get_asset('checkbox_image')
# font = assets.get_asset('font')
# another_font = assets.get_asset('another_font')
# additional_image = assets.get_asset('additional_image')
# Now you can use these assets in your settings menu UI components
