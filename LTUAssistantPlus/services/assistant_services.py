#!/usr/bin/python3

from services.assistant_services_base import AssistantServicesBase
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

class AssistantServices(AssistantServicesBase):
    """Makes various services provided by the assistant available for use by skills."""

    def __init__(self,
        calendar_service: CalendarServiceBase=None,
        listening_service: ListeningServiceBase=None,
        notification_service: NotificationServiceBase=None,
        settings_service: SettingsServiceBase=None,
        speaking_service: SpeakingServiceBase=None,
        user_interaction_service: UserInteractionServiceBase=None,
        text_only_mode: bool=False):
        """Initializes a new instance of the `AssistantServices` class."""
        self.__settings_service = settings_service if settings_service is not None else SettingsService()
        self.__calendar_service = calendar_service if calendar_service is not None else CalendarService()
        self.__notification_service = notification_service if notification_service is not None else NotificationService()
        self.__speak_service = speaking_service if speaking_service is not None else SpeakingService(self.__notification_service, self.__settings_service, text_only_mode)
        self.__listen_service = listening_service if listening_service is not None else ListeningService(text_only_mode)
        self.__interaction_service = user_interaction_service if user_interaction_service is not None else UserInteractionService(self.__speak_service, self.__listen_service)
    
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
