#!/usr/bin/python3

import interactions
import settings
import speaking

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import Skill

class ChangeUserNameSkill(Skill):
    """Lets the user change the name the assistant refers to them by."""

    def __init__(self):
        """Initializes a new instance of the ChangeUserNameSkill class."""
        self._cmd_list = ['call']

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        verb_object = command_input.noun
        alternate_noun = command_input.noun # TODO: Actually get the correct alternate noun.
        new_name = alternate_noun or verb_object
        if new_name:
            settings.set_username(new_name)
            speaking.speak(f"Pleased to meet you, {settings.username}!", True)
            return True
        else:
            return False