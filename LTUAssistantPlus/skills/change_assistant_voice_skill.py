#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
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
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        voice = skill_input.adjective.lower()
        if voice in ("female", "male"):
            services.settings_service.voice = voice
            services.settings_service.save_settings()
            services.user_interaction_service.speak('Okay, I will use a %s voice from now on.' % (voice), True)
        else:
            services.user_interaction_service.speak('I don\'t understand what voice you want')
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass