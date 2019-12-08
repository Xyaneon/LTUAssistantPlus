#!/usr/bin/python3

import user_interface.notification_service
import platform
import settings
import subprocess
from user_interface.speaking_service_base import SpeakingServiceBase

class SpeakingService(SpeakingServiceBase):
    """Provides speaking services."""

    def __init__(self, text_only_mode: bool):
        """Initializes a new instance of the `SpeakingService` class."""
        self.text_only_mode = text_only_mode
        # Initialize private members for platform-specific dependencies
        self._platform_string = platform.system()
        if self._platform_string == "Windows":
            from win32com.client import Dispatch
            self._winspeak = Dispatch("SAPI.SpVoice")
    
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
        user_interface.notification_service.show_notification(message, also_cmd)

    def __say_via_audio(self, message: str):
        """Says the spoken message via system audio."""
        if self._platform_string == "Linux":
            if settings.voice == 'female':
                # Speak using a female voice
                subprocess.call('espeak -v+f1 "' + message + '"', shell=True)
            else:
                # Default to male voice
                subprocess.call('espeak "' + message + '"', shell=True)
        elif self._platform_string == "Windows":
            # TODO: Respect voice configuration settings.
            self._winspeak.speak(message)

if __name__ == "__main__":
    service = SpeakingService(False)
    service.speak("This is a test message from LTU Assistant.", True)