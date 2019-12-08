#!/usr/bin/python3

import datetime

day_values = {'monday': 0,
              'tuesday': 1,
              'wednesday': 2,
              'thursday': 3,
              'friday': 4,
              'saturday': 5,
              'sunday': 6}

DATE_STR_FMT = '%B %d %Y'

def convert_str_to_date(date_str):
    """Converts a string object to a date object."""
    if date_str.lower() == 'tomorrow':
        return datetime.date.today() + datetime.timedelta(days=1)
    elif date_str.lower() == 'today':
        return datetime.date.today()
    elif date_str.lower() == 'yesterday':
        return datetime.date.today() + datetime.timedelta(days=-1)
    elif date_str.lower() in day_values:
        return next_weekday(date_str)
    # Otherwise, process as a three-part date
    part_list = date_str.split()
    day = part_list[1].replace('th', '').replace('rd', '').replace('st', '')
    processed_date_str = ' '.join([part_list[0], day, part_list[2]])
    return datetime.datetime.strptime(processed_date_str, DATE_STR_FMT).date()

# Based on http://stackoverflow.com/a/6558571/3775798
def next_weekday(weekday, d=datetime.datetime.now()):
    """Returns the datetime for the next given day of the week, given as a
    string. Returns None if weekday is not a valid string.
    The second argument is today's date if no datetime is provided."""
    if weekday.lower() not in day_values:
        return None
    days_ahead = day_values[weekday.lower()] - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)