#!/usr/bin/python3

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
import re

def GetPage(url, cookies = None, headers = None, removeTags = False, getredirect=False):
    '''Retrieves the contents of a given URL.'''
    try:
        if cookies:
            req = Request(url, urlencode(headers) if headers else None, {'Cookie':cookies})
        else:
            req = Request(url, urlencode(headers) if headers else None)
        data = urlopen(req, timeout=10)
        page = data.read()
        url = data.geturl()
        if removeTags:
            return re.sub("<.*?>", "", page)
        return url if getredirect else page
    except IOError:
        return None

def GetWeatherInfo():
    '''Retrieves weather information for Southfield, MI.'''
    page = GetPage("http://www.wunderground.com/q/zmw:48033.1.99999?MR=1")
    degreestart = page.find("Southfield, MI | ")
    degrees = page[degreestart+17:degreestart+21]
    status = page[degreestart+29:page.find("\"", degreestart+29)]
    return degrees, status

if __name__ == "__main__":
    degrees, status = GetWeatherInfo()
    print("Degrees: " + degrees)
    print("Status: " + status)