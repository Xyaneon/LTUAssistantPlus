#!/usr/bin/python3

import unittest
from unittest.mock import create_autospec, Mock


from services.assistant_services_base import AssistantServicesBase
from services.settings_service_base import SettingsServiceBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from skills.skill import SkillInput
from skills.change_user_name_skill import ChangeUserNameSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestChangeUserNameSkill(unittest.TestCase):
    """Integration tests for `ChangeUserNameSkill`."""
    def setUp(self):
        self.skill = ChangeUserNameSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = [
            "call me Bob",
            "My name is Bob"
            ]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"ChangeUserNameSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    def test_skillShouldSaveNewUsername(self):
        sentence = "Call me Bob."
        ud = Parse(sentence)
        skill_input = SkillInput(ud, False)

        mock_settings_services = create_autospec(spec=SettingsServiceBase)
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.settings_service.return_value = mock_settings_services
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service

        self.skill.execute_for_command(skill_input, mock_assistant_services)

        # TODO: Figure out how to check that the property setter is being called with the expected value.
        # mock_assistant_services.settings_service.set_username.assert_called_with("Bob")
        mock_assistant_services.settings_service.save_settings.assert_called_with()
    
    def test_skillShouldGreetUserWithNewName(self):
        sentence = "Call me Bob."
        expected_output_speech = "Pleased to meet you, Bob!"
        ud = Parse(sentence)
        skill_input = SkillInput(ud, False)

        mock_settings_services = create_autospec(spec=SettingsServiceBase)
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.settings_service.return_value = mock_settings_services
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service

        self.skill.execute_for_command(skill_input, mock_assistant_services)

        mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, True)