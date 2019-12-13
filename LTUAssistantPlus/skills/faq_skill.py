#!/usr/bin/python3

from ..nlp.universal_dependencies import ParsedUniversalDependencies
from ..services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill


class FAQSkill(Skill):
    """Lets the assistant answer FAQ questions for the user based on LTU website info."""

    def __init__(self):
        """Initializes a new instance of the FAQSkill class."""
        # TODO
        pass

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        return self._is_question_for_curriculum(skill_input) or \
               self._is_question_for_who_has_role(skill_input)

    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        if self._is_question_for_curriculum(skill_input):
            self._handle_question_for_curriculum(skill_input)
        elif self._is_question_for_who_has_role(skill_input):
            self._handle_question_for_who_has_role(skill_input)
        else:
            services.user_interaction_service.speak("Sorry, I cannot answer this kind of question yet.")

    def perform_setup(self, services: AssistantServicesBase):
        """Executes any setup work necessary for this skill before it can be used."""
        if not services.settings_service.faq_initialized:
            self._set_up_database()
            services.settings_service.faq_initialized = True
            services.settings_service.save_settings()
        else:
            print("FAQ database already initialized.")

    # Various helper functions for this skill are to be defined below.

    def _handle_question_for_curriculum(self, skill_input: SkillInput):
        """Handles a question regarding the curriculum."""
        # TODO: Fill this in to have the skill actually process the question and speak the result.
        pass

    def _handle_question_for_who_has_role(self, skill_input: SkillInput):
        """Handles a question regarding which staff member has a role."""
        # TODO: Fill this in to have the skill actually process the question and speak the result.
        pass

    def _is_question_for_curriculum(self, skill_input: SkillInput) -> bool:
        """Determines whether the `SkillInput` is for a question regarding the curriculum."""
        # TODO: Fill this in and return either True or False.
        pass

    def _is_question_for_who_has_role(self, skill_input: SkillInput) -> bool:
        """Determines whether the `SkillInput` is for a question regarding which staff member has a role."""
        # TODO: Fill this in and return either True or False.
        pass

    def _set_up_database(self):
        """Sets up the database used for answering questions by crawling the LTU website."""
        # TODO: Fill this in.
        raise NotImplementedError("The FAQSkill database setup has not been implemented yet.")
