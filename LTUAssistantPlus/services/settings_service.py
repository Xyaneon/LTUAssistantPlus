#!/usr/bin/python3

import configparser
import os

from .settings_service_base import SettingsServiceBase


class SettingsService(SettingsServiceBase):
    """Provides access to the assistant's settings."""

    def __init__(self):
        """Initializes a new instance of the `SettingsService` class."""
        app_data_folder = os.path.join(os.path.expanduser('~'), '.LTUAssistant')
        try:
            os.makedirs(app_data_folder)
        except OSError:
            if not os.path.isdir(app_data_folder):
                raise
        self._settings_ini_path = os.path.join(app_data_folder, 'settings.ini')
        self._config = configparser.ConfigParser()
        if not os.path.isfile(self._settings_ini_path):
            self._create_default_settings_file()
        else:
            self._read_settings_file()

    def _create_default_settings_file(self):
        """Creates a settings file containing the default settings."""
        username = "student"
        voice = "male"
        faq_initialized = False
        self._config['Basic'] = {'username': username,
                                 'voice': voice}
        self._config['Skills'] = {'faq_initialized': faq_initialized}
        self.save_settings()

    def _read_settings_file(self):
        """Reads all settings from a file."""
        self._config.read(self._settings_ini_path)

    def save_settings(self):
        """Save current settings values to the settings file."""
        with open(self._settings_ini_path, 'w') as configfile:
            self._config.write(configfile)

    @property
    def faq_initialized(self) -> str:
        """Whether the FAQ skill has been initialized yet."""
        return self._config.getboolean('Skills', 'faq_initialized')

    @faq_initialized.setter
    def faq_initialized(self, faq_initialized: bool):
        self._config['Skills']['faq_initialized'] = faq_initialized

    @property
    def username(self) -> str:
        """The name the assistant will call the user."""
        return self._config['Basic']['username']

    @username.setter
    def username(self, username: str):
        self._config['Basic']['username'] = username

    @property
    def voice(self) -> str:
        """The voice the assistant will use when speaking."""
        return self._config['Basic']['voice']

    @voice.setter
    def voice(self, voice: str):
        voice_str = voice.lower()
        if voice_str not in ['male', 'female']:
            raise ValueError("The voice must be either 'male' or 'female'.")
        self._config['Basic']['voice'] = voice_str
