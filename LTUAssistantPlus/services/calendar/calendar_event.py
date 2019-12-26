#!/usr/bin/python3

import services.calendar.calendar_util as calendar_util
import datetime

class CalendarEvent():
    """Class for storing calendar event information."""

    def __init__(self, event_str: str='', date_str: str='', start_time_str: str='', end_time_str: str=''):
        """Initialize this CalendarEvent instance."""
        self.event_str = event_str
        self.date = calendar_util.convert_str_to_date(date_str)
        self.start_time_str = start_time_str
        self.end_time_str = end_time_str

    def __str__(self):
        """Returns the string representation of this CalendarEvent."""
        date_str = datetime.datetime.strftime(self.date, calendar_util.DATE_STR_FMT)
        ret = ' '.join([self.event_str, 'on', date_str])
        if self.start_time_str:
            if self.end_time_str:
                ret = ' '.join([ret, 'from', self.start_time_str, 'to',
                                self.end_time_str])
            else:
                ret = ' '.join([ret, 'at', self.start_time_str])
        return ret