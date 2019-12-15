#!/usr/bin/python3

from abc import ABC, abstractmethod, abstractproperty

from services.calendar.calendar_service_base import CalendarServiceBase
from services.settings_service_base import SettingsServiceBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase


class AssistantServicesBase(ABC):
    """Abstract base class for providing assistant services to skills."""

    @property
    @abstractmethod
    def calendar_service(self) -> CalendarServiceBase:
        """The calendar service."""
        pass

    @property
    @abstractmethod
    def settings_service(self) -> SettingsServiceBase:
        """The settings service."""
        pass

    @property
    @abstractmethod
    def user_interaction_service(self) -> UserInteractionServiceBase:
        """The user interaction service."""
        pass
