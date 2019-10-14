#!/usr/bin/python3

from abc import ABC, abstractmethod

from user_interface.listening_service_base import ListeningServiceBase
from user_interface.speaking_service_base import SpeakingServiceBase
from typing import Tuple

class UserInteractionServiceBase(ABC):
    """Abstract base class for a user interaction service."""

    def __init__(self, speak_service: SpeakingServiceBase, listen_service: ListeningServiceBase):
        """Initializes a new instance of the `UserInteractionServiceBase` class."""
        self._speak_service = speak_service
        self._listen_service = listen_service

    @abstractmethod
    def ask_question(self, question, also_cmd=False):
        """Ask the user a question and return the reply as a string."""
        pass

    @abstractmethod
    def greet_user(self, username: str):
        """Greets the user and asks how we can help them."""
        pass

    @abstractmethod
    def greet_user_and_ask_for_command(self, username: str) -> Tuple[bool, str]:
        """
        Greets the user, asks how we can help them, and returns the response as
        a tuple indicating whether listening was successful and what the user said.
        """
        pass

    @abstractmethod
    def listen(self) -> Tuple[bool, str]:
        """Gets a command from the user using the listening service."""
        pass

    @abstractmethod
    def speak(self, message: str, also_cmd: bool = False):
        """Speak the given message using the seaking service."""
        pass

    @abstractmethod
    def tell_user_command_was_not_understood(self):
        """Tells the user their command was not understood."""
        pass

    @abstractmethod
    def tell_user_could_not_be_heard(self):
        """Tells the user they could not be heard."""
        pass