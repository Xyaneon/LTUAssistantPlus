#!/usr/bin/python3

from abc import ABC, abstractmethod, abstractproperty

class SettingsServiceBase(ABC):
    """Abstract base class for access to the assistant's settings."""
    
    @abstractmethod
    def save_settings(self):
        """Save current settings values to the settings file."""
        pass
    
    @abstractproperty
    def username(self) -> str:
        """The name the assistant will call the user."""
        pass
    
    @username.setter
    def username(self, username: str):
        pass
    
    @abstractproperty
    def voice(self) -> str:
        """The voice the assistant will use when speaking."""
        pass
    
    @voice.setter
    def voice(self, voice: str):
        pass
