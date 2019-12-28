#!/usr/bin/python3

import re
import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

class OpenWebsiteSkill(Skill):
    """Lets the assistant open websites for the user."""

    def __init__(self):
        """Initializes a new instance of the OpenWebsiteSkill class."""
        self._cmd_list = ['start', 'open', 'go to', 'take me to']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        deps = skill_input.dependencies
        if deps.verb in ["open", "start"]:
            return True
        elif deps.adj == "open":
            return True
        else:
            return deps.verb in ["go", "take"] and \
                   (deps.noun or deps.pron or deps.propn) and \
                   (deps.adp == "to" or deps.part == "to")
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        requested_site_name = ""
        try:
            requested_site_name = self.__get_requested_site_name_from_input(skill_input)
        except ValueError:
            services.user_interaction_service.speak("I couldn't understand what website you want to open.")
            return
        site_name = ""
        site_url = ""
        if requested_site_name in ['bannerweb', 'banner', 'registration', 'financial aid']:
            site_name = "BannerWeb"
            site_url = "https://www.ltu.edu/bannerweb"
        elif requested_site_name in ['blackboard', 'bb']:
            site_name = "BlackBoard"
            site_url = "https://my.ltu.edu"
        elif requested_site_name in ['library', 'ltu library']:
            site_name = "the LTU Library homepage"
            site_url = "https://www.ltu.edu/library"
        elif requested_site_name in ['help desk', 'helpdesk', 'tech support', 'ehelp']:
            site_name = "the LTU eHelp homepage"
            site_url = "http://www.ltu.edu/ehelp/"
        elif requested_site_name in ['password', 'mypassword']:
            site_name = "MyPassword web service"
            site_url = "https://mypassword.campus.ltu.edu/"
        elif requested_site_name in ['ltu.edu', 'ltu website', 'ltu homepage', 'main ltu website']:
            site_name = "the main LTU website"
            site_url = "http://www.ltu.edu"
        elif requested_site_name in ['email', 'webmail', 'mail', 'gmail']:
            site_name = "Gmail"
            site_url = "https://gmail.com"
        elif requested_site_name in ['calendar', 'schedule', 'events']:
            site_name = "Google Calendar"
            site_url = "https://calendar.google.com"
        elif requested_site_name in ['ltu events', 'ltu event']:
            site_name = "ltu events"
            site_url = "http://www.ltu.edu/myltu/calendar.asp"
        else:
            services.user_interaction_service.speak("I don't recognize the website you want to open.")
            return
        self.__open_site(site_name, site_url, services, skill_input.verbose)
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass

    def __get_requested_site_name_from_input(self, skill_input: SkillInput) -> str:
        """Retrieves the requested site name from the input."""
        leading_commands = "(?:" + "|".join(self._cmd_list) + r")(?:\s+the)?"
        pattern = leading_commands + r"\s+(.*)"
        retrieval_regex = re.compile(pattern, re.IGNORECASE)
        site_name = re.match(retrieval_regex, skill_input.sentence).group(1)
        if not site_name or site_name == "":
            raise ValueError("Could not retrieve the site name from the user's request.")
        return site_name
    
    def __open_site(self, site_name: str, site_url: str, services: AssistantServicesBase, verbose: bool):
        """Announces opening a site and then actually opens it."""
        services.user_interaction_service.speak(f"Opening {site_name}...", verbose)
        webbrowser.open(site_url)