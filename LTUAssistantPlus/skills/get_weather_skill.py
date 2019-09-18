#!/usr/bin/python3

import calendardb
import interactions
import speaking
import web

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import Skill

class GetWeatherSkill(Skill):
    """Lets the assistant get the weather for the user."""

    def __init__(self):
        """Initializes a new instance of the GetWeatherSkill class."""
        self._cmd_list = ['what is', 'tell']

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        verb_object = (command_input.noun or None) and command_input.noun.lower()
        return verb in self._cmd_list and verb_object == "weather"
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        degrees, status = web.GetWeatherInfo()
        speaking.speak("It is " + degrees + " degrees and " + status.lower() + ".", verbose)