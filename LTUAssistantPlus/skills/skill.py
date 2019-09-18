#!/usr/bin/python3

from abc import ABC, abstractmethod
from nlp.universal_dependencies import ParsedUniversalDependencies

class Skill(ABC):
    """Abstract base class for assistant skills."""

    @abstractmethod
    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        pass
    
    @abstractmethod
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        pass