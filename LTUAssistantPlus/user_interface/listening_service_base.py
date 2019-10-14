#!/usr/bin/python3

from abc import ABC, abstractmethod

from typing import Tuple

class ListeningServiceBase(ABC):
    """Abstract base class for a listening service."""

    @abstractmethod
    def listen(self) -> Tuple[bool, str]:
        """Gets a command from the user, either via the microphone or command line
        if text-only mode was specified."""
        pass