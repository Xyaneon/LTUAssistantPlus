#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

class TellTimeSkill(Skill):
    """Lets the assistant tell the user the current time."""

    def __init__(self):
        """Initializes a new instance of the TellTimeSkill class."""
        self._cmd_list = ['what is', 'tell']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        verb_object = (skill_input.verb_object or None) and skill_input.verb_object.lower()
        if verb in self._cmd_list and verb_object == "time":
            return True
        else:
            return skill_input.dependencies.pron == "what" and \
                   skill_input.dependencies.aux == "be" and \
                   skill_input.dependencies.noun == "time"
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        services.user_interaction_service.speak(f"It is currently {services.calendar_service.get_current_time()}.", True)
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass