#!/usr/bin/python3

import csv
import datetime
import os

from typing import List

day_values = {'monday': 0,
              'tuesday': 1,
              'wednesday': 2,
              'thursday': 3,
              'friday': 4,
              'saturday': 5,
              'sunday': 6}
DATE_STR_FMT = '%B %d %Y'

# Based on http://stackoverflow.com/a/6558571/3775798
def _next_weekday(weekday, d=datetime.datetime.now()):
    """Returns the datetime for the next given day of the week, given as a
    string. Returns None if weekday is not a valid string.
    The second argument is today's date if no datetime is provided."""
    if weekday.lower() not in day_values:
        return None
    days_ahead = day_values[weekday.lower()] - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def _convert_str_to_date(date_str):
    """Converts a string object to a date object."""
    if date_str.lower() == 'tomorrow':
        return datetime.date.today() + datetime.timedelta(days=1)
    elif date_str.lower() == 'today':
        return datetime.date.today()
    elif date_str.lower() == 'yesterday':
        return datetime.date.today() + datetime.timedelta(days=-1)
    elif date_str.lower() in day_values:
        return _next_weekday(date_str)
    # Otherwise, process as a three-part date
    part_list = date_str.split()
    day = part_list[1].replace('th', '').replace('rd', '').replace('st', '')
    processed_date_str = ' '.join([part_list[0], day, part_list[2]])
    return datetime.datetime.strptime(processed_date_str, DATE_STR_FMT).date()

class CalendarEvent():
    """Class for storing calendar event information."""

    def __init__(self, event_str: str='', date_str: str='', start_time_str: str='', end_time_str: str=''):
        """Initialize this CalendarEvent instance."""
        self.event_str = event_str
        self.date = _convert_str_to_date(date_str)
        self.start_time_str = start_time_str
        self.end_time_str = end_time_str

    def __str__(self):
        """Returns the string representation of this CalendarEvent."""
        date_str = datetime.datetime.strftime(self.date, DATE_STR_FMT)
        ret = ' '.join([self.event_str, 'on', date_str])
        if self.start_time_str:
            if self.end_time_str:
                ret = ' '.join([ret, 'from', self.start_time_str, 'to',
                                self.end_time_str])
            else:
                ret = ' '.join([ret, 'at', self.start_time_str])
        return ret

class CalendarService():
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
            requested_date = _convert_str_to_date(date_str)
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
