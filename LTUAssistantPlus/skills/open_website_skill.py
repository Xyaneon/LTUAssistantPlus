#!/usr/bin/python3

import interactions
import speaking
import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import SkillInput, Skill

class OpenWebsiteSkill(Skill):
    """Lets the assistant open websites for the user."""

    def __init__(self):
        """Initializes a new instance of the OpenWebsiteSkill class."""
        self._cmd_list = ['start', 'open', 'go', 'go to', 'browse', 'browse to', 'launch', 'take to', 'show']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput):
        """Executes this skill on the given command input."""
        verb_object = skill_input.dependencies.noun or skill_input.dependencies.propn
        if verb_object is None:
            speaking.speak("I couldn't understand what website you want to open.")
            return
        site_name = verb_object.lower()
        if site_name in ['bannerweb', 'banner', 'registration', 'financial aid']:
            self.__open_site("BannerWeb", "https://www.ltu.edu/bannerweb", skill_input.verbose)
        elif site_name in ['blackboard', 'bb']:
            self.__open_site("BlackBoard", "https://my.ltu.edu", skill_input.verbose)
        elif site_name in ['library', 'ltu library']:
            self.__open_site("the LTU Library homepage", "https://www.ltu.edu/library", skill_input.verbose)
        elif site_name in ['help desk', 'helpdesk', 'tech support', 'ehelp']:
            self.__open_site("the LTU eHelp homepage", "http://www.ltu.edu/ehelp/", skill_input.verbose)
        elif site_name in ['password', 'mypassword']:
            self.__open_site("MyPassword web service", "https://mypassword.campus.ltu.edu/", skill_input.verbose)
        elif site_name in ['ltu.edu', 'ltu website', 'ltu homepage']:
            self.__open_site("the main LTU website", "http://www.ltu.edu", skill_input.verbose)
        elif site_name in ['email', 'webmail', 'mail', 'gmail']:
            self.__open_site("Gmail", "https://gmail.com", skill_input.verbose)
        elif site_name in ['calendar', 'schedule', 'events']:
            self.__open_site("Google Calendar", "https://calendar.google.com", skill_input.verbose)
        elif site_name in ['ltu events', 'ltu event']:
            self.__open_site("ltu events", "http://www.ltu.edu/myltu/calendar.asp", skill_input.verbose)
        else:
            speaking.speak("I don't recognize the website you want to open.")
    
    def __open_site(self, site_name: str, site_url: str, verbose: bool):
        """Announces opening a site and then actually opens it."""
        speaking.speak(f"Opening {site_name}...", verbose)
        webbrowser.open(site_url)