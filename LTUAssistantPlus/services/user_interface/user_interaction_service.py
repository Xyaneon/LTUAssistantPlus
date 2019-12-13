#!/usr/bin/python3

from services.user_interface.listening_service_base import ListeningServiceBase
from services.user_interface.speaking_service_base import SpeakingServiceBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from typing import Tuple

class UserInteractionService(UserInteractionServiceBase):
    """Provides user interaction services."""

    def __init__(self, speak_service: SpeakingServiceBase, listen_service: ListeningServiceBase):
        """Initializes a new instance of the `UserInteractionService` class."""
        super().__init__(speak_service, listen_service)

    def ask_question(self, question, also_cmd=False):
        """Ask the user a question and return the reply as a string."""
        self.speak(question, also_cmd)
        num_tries = 3
        for _ in range(0, num_tries):
            (success, sentence) = self.listen()
            if success:
                return sentence
            else:
                self.speak('I\'m sorry, could you repeat that?', also_cmd)
        self.speak('I\'m sorry, I could not understand you.', also_cmd)
        return ''

    def greet_user(self, username: str):
        """Greets the user and asks how we can help them."""
        greeting_str = f"Hi {username}! What can I help you with?"
        self.speak(greeting_str, True)

    def greet_user_and_ask_for_command(self, username: str) -> Tuple[bool, str]:
        """
        Greets the user, asks how we can help them, and returns the response as
        a tuple indicating whether listening was successful and what the user said.
        """
        self.greet_user(username)
        return self.listen()
    
    def listen(self) -> Tuple[bool, str]:
        """Gets a command from the user using the listening service."""
        return self._listen_service.listen()

    def speak(self, message: str, also_cmd: bool = False):
        """Speak the given message using the seaking service."""
        self._speak_service.speak(message, also_cmd)

    def tell_user_command_was_not_understood(self):
        """Tells the user their command was not understood."""
        self.speak("Sorry, I don't understand what you want.", True)

    def tell_user_could_not_be_heard(self):
        """Tells the user they could not be heard."""
        self.speak("Sorry, I wasn't able to hear you.", True)