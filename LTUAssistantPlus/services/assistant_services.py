#!/usr/bin/python3

from services.calendar.calendar_service_base import CalendarServiceBase
from services.calendar.calendar_service import CalendarService
from services.settings_service_base import SettingsServiceBase
from services.settings_service import SettingsService
from services.user_interface.listening_service_base import ListeningServiceBase
from services.user_interface.listening_service import ListeningService
from services.user_interface.notification_service_base import NotificationServiceBase
from services.user_interface.notification_service import NotificationService
from services.user_interface.speaking_service_base import SpeakingServiceBase
from services.user_interface.speaking_service import SpeakingService
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from services.user_interface.user_interaction_service import UserInteractionService

class AssistantServices():
    """Makes various services provided by the assistant available for use by skills."""

    def __init__(self, text_only_mode: bool):
        """Initializes a new instance of the `AssistantServices` class."""
        self.__settings_service = SettingsService()
        self.__calendar_service = CalendarService()
        self.__notification_service = NotificationService()
        self.__speak_service = SpeakingService(self.__notification_service, self.__settings_service, text_only_mode)
        self.__listen_service = ListeningService(text_only_mode)
        self.__interaction_service = UserInteractionService(self.__speak_service, self.__listen_service)
    
    @property
    def calendar_service(self) -> CalendarServiceBase:
        """The calendar service."""
        return self.__calendar_service
    
    @property
    def settings_service(self) -> SettingsServiceBase:
        """The settings service."""
        return self.__settings_service
    
    @property
    def user_interaction_service(self) -> UserInteractionServiceBase:
        """The user interaction service."""
        return self.__interaction_service
