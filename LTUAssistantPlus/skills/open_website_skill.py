#!/usr/bin/python3

import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services import AssistantServices
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
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServices):
        """Executes this skill on the given command input."""
        verb_object = skill_input.dependencies.noun or skill_input.dependencies.propn
        if verb_object is None:
            services.user_interaction_service.speak("I couldn't understand what website you want to open.")
            return
        requested_site_name = verb_object.lower()
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
        elif requested_site_name in ['ltu.edu', 'ltu website', 'ltu homepage']:
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
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass
    
    def __open_site(self, site_name: str, site_url: str, services: AssistantServices, verbose: bool):
        """Announces opening a site and then actually opens it."""
        services.user_interaction_service.speak(f"Opening {site_name}...", verbose)
        webbrowser.open(site_url)