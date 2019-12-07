#!/usr/bin/python3

import settings

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
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
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        alternate_noun = skill_input.noun # TODO: Actually get the correct alternate noun.
        new_name = alternate_noun or verb_object
        if new_name:
            settings.set_username(new_name)
            user_interaction_service.speak(f"Pleased to meet you, {settings.username}!", True)
            return True
        else:
            return False
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass