#!/usr/bin/python3

from abc import ABC, abstractmethod

class SpeakingServiceBase(ABC):
    "Abstract base class for a speaking service."

    @abstractmethod
    def speak(self, message: str, also_cmd: bool = False):
        """Speak the given message using the text-to-speech backend."""
        pass