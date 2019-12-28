#!/usr/bin/python3

from abc import ABC, abstractmethod
from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase

class SkillInput(object):
    """Represents the input data for a Skill at its entry point."""

    def __init__(self, sentence: str, dependencies: ParsedUniversalDependencies, verbose: bool = False):
        """Initializes a new instance of the `SkillInput` class."""
        if sentence is None:
            raise TypeError("sentence cannot be None")
        self.sentence = sentence
        if dependencies is None:
            raise TypeError("dependencies cannot be None")
        self.dependencies = dependencies
        self.verb = (dependencies.verb or None) and dependencies.verb.lower()
        self.verb_object = dependencies.noun or dependencies.propn
        self.alternate_noun = dependencies.noun # TODO: Actually get the correct alternate noun.
        self.adjective = (dependencies.adj or None) and dependencies.adj.lower()
        self.verbose = verbose

class Skill(ABC):
    """Abstract base class for assistant skills."""

    @abstractmethod
    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        pass
    
    @abstractmethod
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        pass

    @abstractmethod
    def perform_setup(self, services: AssistantServicesBase):
        """Executes any setup work necessary for this skill before it can be used."""
        pass