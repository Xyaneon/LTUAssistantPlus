#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

class ChangeUserNameSkill(Skill):
    """Lets the user change the name the assistant refers to them by."""

    def __init__(self):
        """Initializes a new instance of the ChangeUserNameSkill class."""
        pass

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        return skill_input.dependencies.verb == "call" or \
               (skill_input.dependencies.noun == "name" and skill_input.dependencies.aux == "be")
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        new_name = skill_input.dependencies.propn
        if new_name:
            services.settings_service.username = new_name
            services.settings_service.save_settings()
            services.user_interaction_service.speak(f"Pleased to meet you, {new_name}!", True)
            return True
        else:
            return False
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass