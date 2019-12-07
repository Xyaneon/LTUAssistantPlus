#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from .skill import SkillInput, Skill

class FAQSkill(Skill):
    """Lets the assistant answer FAQ questions for the user based on LTU website info."""

    def __init__(self):
        """Initializes a new instance of the FAQSkill class."""
        # TODO
        self._cmd_list = ['what is', 'who is']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        # TODO
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        # TODO
        pass

    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        # TODO: Perform web crawling and database setup here.
        raise NotImplementedError("The FAQSkill setup has not been implemented yet.")