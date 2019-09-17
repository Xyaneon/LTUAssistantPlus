#!/usr/bin/python3

import interactions
import speaking
import webbrowser

from nlp.universal_dependencies import ParsedUniversalDependencies
from skill import Skill

class SendEmailSkill(Skill):
    """Lets the assistant send emails for the user."""

    def __init__(self):
        """Initializes a new instance of the SendEmailSkill class."""
        self._cmd_list = ['email', 'compose', 'compose to', 'send', 'send to', "write", "write to"]

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        verb_object = command_input.noun
        recipient_info = verb_object
        if recipient_info and recipient_info.find("@") != -1:
            recipient = 'mailto:' + recipient_info  # Open default email client
        else:
            recipient = 'https://mail.google.com/mail/u/0/#compose' # Gmail
        speaking.speak('Composing an email...', verbose)
        webbrowser.open(recipient)