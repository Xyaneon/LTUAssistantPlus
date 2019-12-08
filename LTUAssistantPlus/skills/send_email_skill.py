#!/usr/bin/python3

import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services import AssistantServices
from .skill import SkillInput, Skill

class SendEmailSkill(Skill):
    """Lets the assistant send emails for the user."""

    def __init__(self):
        """Initializes a new instance of the SendEmailSkill class."""
        self._cmd_list = ['email', 'compose', 'compose to', 'send', 'send to', "write", "write to"]

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServices):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        recipient_info = verb_object
        if recipient_info and recipient_info.find("@") != -1:
            recipient = 'mailto:' + recipient_info  # Open default email client
        else:
            recipient = 'https://mail.google.com/mail/u/0/#compose' # Gmail
        services.user_interaction_service.speak('Composing an email...', skill_input.verbose)
        webbrowser.open(recipient)
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass