#!/usr/bin/python3

import settings

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from .skill import SkillInput, Skill

class ChangeAssistantVoiceSkill(Skill):
    """Lets the user change the assistant's voice."""

    def __init__(self):
        """Initializes a new instance of the ChangeAssistantVoiceSkill class."""
        self._cmd_list = ['use']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        adjective = skill_input.adj.lower()
        voice = adjective
        if voice in ("female", "male"):
            settings.set_voice(voice)
            user_interaction_service.speak('Okay, I will use a %s voice from now on.' % (voice), True)
        else:
            user_interaction_service.speak('I don\'t understand what voice you want')