#!/usr/bin/python3

import re
import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

from typing import List

class _SupportedWebsite():
    """Helper class for `OpenWebsiteSkill` containing data for a supported website."""

    def __init__(self, request_names: List[str], site_name: str, site_url: str):
        """Initializes a new instance of the `_SupportedWebsite` class."""
        self.request_names = request_names
        self.site_name = site_name
        self.site_url = site_url

class OpenWebsiteSkill(Skill):
    """Lets the assistant open websites for the user."""

    def __init__(self):
        """Initializes a new instance of the OpenWebsiteSkill class."""
        self._supported_websites = [
            _SupportedWebsite(
                ['bannerweb', 'banner', 'registration', 'financial aid'],
                "BannerWeb",
                "https://www.ltu.edu/bannerweb"
            ),
            _SupportedWebsite(
                ['blackboard', 'bb'],
                "BlackBoard",
                "https://my.ltu.edu"
            ),
            _SupportedWebsite(
                ['library', 'ltu library'],
                "the LTU Library homepage",
                "https://www.ltu.edu/library"
            ),
            _SupportedWebsite(
                ['help desk', 'helpdesk', 'tech support', 'ehelp'],
                "the LTU eHelp homepage",
                "http://www.ltu.edu/ehelp/"
            ),
            _SupportedWebsite(
                ['password', 'mypassword'],
                "MyPassword web service",
                "https://mypassword.campus.ltu.edu/"
            ),
            _SupportedWebsite(
                ['ltu.edu', 'ltu website', 'ltu homepage', 'main ltu website'],
                "the main LTU website",
                "http://www.ltu.edu"
            ),
            _SupportedWebsite(
                ['email', 'webmail', 'mail', 'gmail'],
                "Gmail",
                "https://gmail.com"
            ),
            _SupportedWebsite(
                ['calendar', 'schedule', 'events'],
                "Google Calendar",
                "https://calendar.google.com"
            ),
            _SupportedWebsite(
                ['ltu events', 'ltu event'],
                "ltu events",
                "http://www.ltu.edu/myltu/calendar.asp"
            )
        ]

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

        for website in self._supported_websites:
            if requested_site_name in website.request_names:
                self.__open_site(website.site_name, website.site_url, services, skill_input.verbose)
                return
        services.user_interaction_service.speak("I don't recognize the website you want to open.")
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass

    def __get_requested_site_name_from_input(self, skill_input: SkillInput) -> str:
        """Retrieves the requested site name from the input."""
        cmd_list = ['start', 'open', 'go to', 'take me to']
        leading_commands = "(?:" + "|".join(cmd_list) + r")(?:\s+the)?"
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