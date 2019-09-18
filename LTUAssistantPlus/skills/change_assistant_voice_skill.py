#!/usr/bin/python3

import interactions
import settings
import speaking

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import Skill

class ChangeAssistantVoiceSkill(Skill):
    """Lets the user change the assistant's voice."""

    def __init__(self):
        """Initializes a new instance of the ChangeAssistantVoiceSkill class."""
        self._cmd_list = ['use']

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        adjective = command_input.adj.lower()
        voice = adjective
        if voice in ("female", "male"):
            settings.set_voice(voice)
            speaking.speak('Okay, I will use a %s voice from now on.' % (voice), True)
        else:
            speaking.speak('I don\'t understand what voice you want')