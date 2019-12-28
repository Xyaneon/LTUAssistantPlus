#!/usr/bin/python3

import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

class SendEmailSkill(Skill):
    """Lets the assistant send emails for the user."""

    def __init__(self):
        """Initializes a new instance of the SendEmailSkill class."""
        self._cmd_list = ['email', 'compose', 'compose to', 'send', 'send to', "write", "write to"]

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        deps = skill_input.dependencies
        if verb in self._cmd_list:
            return True
        else:
            return deps.noun == "email" and \
                   self._string_is_an_email_address(deps.x)
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        recipient_info = skill_input.dependencies.x
        if self._string_is_an_email_address(recipient_info):
            email_url = 'mailto:' + recipient_info  # Open default email client
        else:
            email_url = 'https://mail.google.com/mail/u/0/#compose' # Gmail
        services.user_interaction_service.speak('Composing an email...', skill_input.verbose)
        webbrowser.open(email_url)
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass

    def _string_is_an_email_address(self, string_to_check: str) -> bool:
        """Returns `True` if the provided string is an email address."""
        return string_to_check and string_to_check.find("@") != -1