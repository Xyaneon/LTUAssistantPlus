#!/usr/bin/python3

import platform
import subprocess
from services.settings_service import SettingsService
from services.user_interface.notification_service_base import NotificationServiceBase
from services.user_interface.speaking_service_base import SpeakingServiceBase

class SpeakingService(SpeakingServiceBase):
    """Provides speaking services."""

    def __init__(self, notification_service: NotificationServiceBase, settings_service: SettingsService, text_only_mode: bool):
        """Initializes a new instance of the `SpeakingService` class."""
        self.text_only_mode = text_only_mode
        # Initialize private members for platform-specific dependencies
        self._platform_string = platform.system()
        if self._platform_string == "Windows":
            from win32com.client import Dispatch
            self._winspeak = Dispatch("SAPI.SpVoice")
        self._notification_service = notification_service
        self._settings_service = settings_service
    
    def speak(self, message: str, also_cmd: bool = False):
        """Speak the given message using the text-to-speech backend."""
        if also_cmd or self.text_only_mode:
            self.__say_in_terminal(message)
        self.__say_in_notification(message, also_cmd)
        if not self.text_only_mode:
            self.__say_via_audio(message)

    def __say_in_terminal(self, message: str):
        """Shows the spoken message in the CLI."""
        print(message)

    def __say_in_notification(self, message: str, also_cmd: bool):
        """Shows the spoken message in a system notification."""
        if self._notification_service is not None:
            self._notification_service.show_notification(message, also_cmd)

    def __say_via_audio(self, message: str):
        """Says the spoken message via system audio."""
        if self._platform_string == "Linux":
            if self._settings_service.voice == 'female':
                # Speak using a female voice
                subprocess.call('espeak -v+f1 "' + message + '"', shell=True)
            else:
                # Default to male voice
                subprocess.call('espeak "' + message + '"', shell=True)
        elif self._platform_string == "Windows":
            voices = self._winspeak.GetVoices()
            if self._settings_service.voice == 'female':
                # Speak using a female voice
                self._winspeak.Voice = voices.Item(1)
            else:
                # Default to male voice
                self._winspeak.Voice = voices.Item(0)
            self._winspeak.Speak(message)

if __name__ == "__main__":
    service = SpeakingService(None, None, False)
    service.speak("This is a test message from LTU Assistant.", True)