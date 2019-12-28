#!/usr/bin/python3

import unittest
from unittest.mock import create_autospec, Mock

from services.assistant_services_base import AssistantServicesBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from skills.skill import SkillInput
from skills.room_finder_skill import RoomFinderSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestRoomFinderSkill(unittest.TestCase):
    """Integration tests for `RoomFinderSkill`."""
    def setUp(self):
        self.skill = RoomFinderSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = [
            "find A101",
            "find room A101",
            "where is A101",
            "where is room A101"
        ]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"RoomFinderSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    def test_skillShouldGiveCorrectOutput(self):
        sentence = "where is room A101"
        expected_output_speech = "Your room is in the Architecture Building on floor 1."
        ud = Parse(sentence)
        skill_input = SkillInput(sentence, ud, False)
        
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service

        self.skill.execute_for_command(skill_input, mock_assistant_services)

        mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, False)
    
    def test_skillShouldRejectInvalidBuildingLetter(self):
        sentence = "where is room Z101"
        expected_output_speech = "Sorry, I don't think you provided me with a valid room number."
        ud = Parse(sentence)
        skill_input = SkillInput(sentence, ud, False)
        
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service

        self.skill.execute_for_command(skill_input, mock_assistant_services)

        mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, False)
    
    def test_skillShouldRejectMissingRoomNumber(self):
        sentence = "where is room"
        expected_output_speech = "Sorry, I don't think you provided me with a valid room number."
        ud = Parse(sentence)
        skill_input = SkillInput(sentence, ud, False)
        
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service

        self.skill.execute_for_command(skill_input, mock_assistant_services)

        mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, False)
