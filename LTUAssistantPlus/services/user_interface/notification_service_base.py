#!/usr/bin/python3

from abc import ABC, abstractmethod

class NotificationServiceBase(ABC):
    "Abstract base class for a notification service."

    @abstractmethod
    def show_notification(self, message: str, also_cmd: bool = False):
        """Show spoken words from the assistant as a notification."""
        pass