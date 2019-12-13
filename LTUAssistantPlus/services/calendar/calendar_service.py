#!/usr/bin/python3

import csv
import datetime
import os
import services.calendar.calendar_util as calendar_util

from typing import List

from services.calendar.calendar_event import CalendarEvent
from services.calendar.calendar_service_base import CalendarServiceBase

class CalendarService(CalendarServiceBase):
    """Provides date, time and schedule services to skills."""

    def __init__(self):
        """Initializes a new instance of the `CalendarService` class."""
        folder = os.path.join(os.path.expanduser('~'), '.LTUAssistant')
        try:
            os.makedirs(folder)
        except OSError:
            if not os.path.isdir(folder):
                raise
        self._calendar_csv_path = os.path.join(folder, 'calendar.csv')

    def read_events(self) -> List[CalendarEvent]:
        """Returns a list of CalendarEvents from the calendar DB CSV file."""
        event_list = []
        with open(self._calendar_csv_path, 'r') as calendar_csv:
            calreader = csv.reader(calendar_csv, delimiter=',', quotechar='"')
            for row in calreader:
                print(', '.join(row))
                event_list.append(CalendarEvent(row[0], row[1], row[2], row[3]))
        return event_list

    def get_events_for_date(self, date_str: str=''):
        """Returns a list of CalendarEvents scheduled for today. If date_str is
        not given, default to today's date (see get_todays_events())."""
        event_list = self.read_events()
        if date_str:
            requested_date = calendar_util.convert_str_to_date(date_str)
        else:
            requested_date = datetime.datetime.today().date()
        return [event for event in event_list if event.date == requested_date]

    def get_todays_events(self):
        """Returns a list of CalendarEvents scheduled for today."""
        event_list = self.read_events()
        todays_date = datetime.datetime.today().date()
        return [event for event in event_list if event.date == todays_date]

    def add_event(self, ce: CalendarEvent):
        """Adds a new event in list form to the calendar DB CSV file.
        Takes a CalendarEvent object."""
        with open(self._calendar_csv_path, 'a') as calendar_csv:
            calwriter = csv.writer(calendar_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            cal_row = [ce.event_str,
                       ce.date.strftime('%B %d %Y'),
                       ce.start_time_str,
                       ce.end_time_str]
            calwriter.writerow(cal_row)

    def get_current_time(self) -> str:
        """Returns a printable string for the current time."""
        current_time = datetime.datetime.now().time()
        return current_time.strftime('%I:%M %p')

    def get_current_date(self) -> str:
        """Returns a printable string for the current time."""
        current_time = datetime.datetime.now().date()
        return current_time.strftime('%B %d, %Y')
