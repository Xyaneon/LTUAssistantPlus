#!/usr/bin/python3

import interactions
import speaking
import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from skill import Skill

class OpenWebsiteSkill(Skill):
    """Lets the assistant open websites for the user."""

    def __init__(self):
        """Initializes a new instance of the OpenWebsiteSkill class."""
        self._cmd_list = ['start', 'open', 'go', 'go to', 'browse', 'browse to', 'launch', 'take to', 'show']

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        verb_object = command_input.noun
        site_name = verb_object.lower()
        if site_name in ['bannerweb', 'banner', 'registration', 'financial aid']:
            self.__open_site("BannerWeb", "https://www.ltu.edu/bannerweb", verbose)
        elif site_name in ['blackboard', 'bb']:
            self.__open_site("BlackBoard", "https://my.ltu.edu", verbose)
        elif site_name in ['library', 'ltu library']:
            self.__open_site("the LTU Library homepage", "https://www.ltu.edu/library", verbose)
        elif site_name in ['help desk', 'helpdesk', 'tech support', 'ehelp']:
            self.__open_site("the LTU eHelp homepage", "http://www.ltu.edu/ehelp/", verbose)
        elif site_name in ['password', 'mypassword']:
            self.__open_site("MyPassword web service", "https://mypassword.campus.ltu.edu/", verbose)
        elif site_name in ['ltu.edu', 'ltu website', 'ltu homepage']:
            self.__open_site("the main LTU website", "http://www.ltu.edu", verbose)
        elif site_name in ['email', 'webmail', 'mail', 'gmail']:
            self.__open_site("Gmail", "https://gmail.com", verbose)
        elif site_name in ['calendar', 'schedule', 'events']:
            self.__open_site("Google Calendar", "https://calendar.google.com", verbose)
        elif site_name in ['ltu events', 'ltu event']:
            self.__open_site("ltu events", "http://www.ltu.edu/myltu/calendar.asp", verbose)
        else:
            speaking.speak("I couldn't understand what website you want to open")
    
    def __open_site(self, site_name: str, site_url: str, verbose: bool):
        """Announces opening a site and then actually opens it."""
        speaking.speak(f"Opening {site_name}...", verbose)
        webbrowser.open(site_url)