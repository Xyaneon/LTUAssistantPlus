#!/usr/bin/python3

from abc import ABC, abstractmethod

from typing import List

from services.calendar.calendar_event import CalendarEvent

class CalendarServiceBase(ABC):
    """Provides date, time and schedule services to skills."""

    @abstractmethod
    def read_events(self) -> List[CalendarEvent]:
        """Returns a list of CalendarEvents from the calendar DB CSV file."""
        pass

    @abstractmethod
    def get_events_for_date(self, date_str: str=''):
        """Returns a list of CalendarEvents scheduled for today. If date_str is
        not given, default to today's date (see get_todays_events())."""
        pass

    @abstractmethod
    def get_todays_events(self):
        """Returns a list of CalendarEvents scheduled for today."""
        pass

    @abstractmethod
    def add_event(self, ce: CalendarEvent):
        """Adds a new event in list form to the calendar DB CSV file.
        Takes a CalendarEvent object."""
        pass

    @abstractmethod
    def get_current_time(self) -> str:
        """Returns a printable string for the current time."""
        pass

    @abstractmethod
    def get_current_date(self) -> str:
        """Returns a printable string for the current time."""
        pass