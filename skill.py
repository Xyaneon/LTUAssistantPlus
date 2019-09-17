#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies

class Skill(object):
    """Base class for assistant skills."""

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        return False
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        pass