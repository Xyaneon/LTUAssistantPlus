#!/usr/bin/python3

import interactions
import settings
import user_interface.speaking

from nlp.universal_dependencies import ParsedUniversalDependencies
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
    
    def execute_for_command(self, skill_input: SkillInput):
        """Executes this skill on the given command input."""
        adjective = skill_input.adj.lower()
        voice = adjective
        if voice in ("female", "male"):
            settings.set_voice(voice)
            user_interface.speaking.speak('Okay, I will use a %s voice from now on.' % (voice), True)
        else:
            user_interface.speaking.speak('I don\'t understand what voice you want')