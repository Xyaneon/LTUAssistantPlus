#!/usr/bin/python3

import interactions
import settings
import user_interface.speaking

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import SkillInput, Skill

class ChangeUserNameSkill(Skill):
    """Lets the user change the name the assistant refers to them by."""

    def __init__(self):
        """Initializes a new instance of the ChangeUserNameSkill class."""
        self._cmd_list = ['call']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        alternate_noun = skill_input.noun # TODO: Actually get the correct alternate noun.
        new_name = alternate_noun or verb_object
        if new_name:
            settings.set_username(new_name)
            user_interface.speaking.speak(f"Pleased to meet you, {settings.username}!", True)
            return True
        else:
            return False