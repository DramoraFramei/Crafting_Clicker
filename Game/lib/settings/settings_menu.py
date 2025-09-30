# Settings Menu
# This file contains the settings menu for the game.
# It allows the player to adjust various settings such as sound volume, graphics
# quality, and control preferences.
# The settings are saved to a configuration file and loaded when the game
# starts.
# The settings menu is accessible from the main menu and can be navigated using
# the mouse or keyboard.
# The settings can be found in the 'settings.json' file in the same directory
# as this script.
import os
import json
import pygame
from pygame.locals import * # type: ignore
from Game.lib.settings import settings as Settings
from Game.lib.assets.SettingsMenuAssets import SettingsMenuAssets

# Create a settings menu class
class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings.load_settings()
        self.assets = SettingsMenuAssets()
        self.buttons = []
        self.sliders = []
        self.dropdowns = []
        self.checkboxes = []
        self.create_ui_elements()
        self.running = True

    def create_ui_elements(self):
        # Create buttons
        self.buttons.append(Button("Save", (100, 400), self.save_settings))
        self.buttons.append(Button("Cancel", (300, 400), self.cancel_settings))

        # Create sliders
        self.sliders.append(Slider("Sound Volume", (100, 100), 0, 100, self.settings['sound_volume'], self.update_sound_volume))
        self.sliders.append(Slider("Music Volume", (100, 150), 0, 100, self.settings['music_volume'], self.update_music_volume))

        # Create dropdowns
        self.dropdowns.append(Dropdown("Graphics Quality", (100, 200), ["Low", "Medium", "High"], self.settings['graphics_quality'], self.update_graphics_quality))

        # Create checkboxes
        self.checkboxes.append(Checkbox("Fullscreen", (100, 250), self.settings['fullscreen'], self.update_fullscreen))

    def update_sound_volume(self, value):
        self.settings['sound_volume'] = value

    def update_music_volume(self, value):
        self.settings['music_volume'] = value

    def update_graphics_quality(self, value):
        self.settings['graphics_quality'] = value

    def update_fullscreen(self, value):
        self.settings['fullscreen'] = value

    def save_settings(self):
        Settings.save_settings(self.settings)
        self.running = False

    def cancel_settings(self):
        self.running = False

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                for button in self.buttons:
                    button.handle_event(event)
                for slider in self.sliders:
                    slider.handle_event(event)
                for dropdown in self.dropdowns:
                    dropdown.handle_event(event)
                for checkbox in self.checkboxes:
                    checkbox.handle_event(event)

            self.screen.fill((0, 0, 0))
            for button in self.buttons:
                button.draw(self.screen)
            for slider in self.sliders:
                slider.draw(self.screen)
            for dropdown in self.dropdowns:
                dropdown.draw(self.screen)
            for checkbox in self.checkboxes:
                checkbox.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)
