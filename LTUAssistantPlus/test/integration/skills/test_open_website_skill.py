#!/usr/bin/python3

import unittest
from unittest import mock
from unittest.mock import create_autospec, Mock, patch
import webbrowser

from services.assistant_services_base import AssistantServicesBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from skills.skill import SkillInput
from skills.open_website_skill import OpenWebsiteSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

def webbrowser_open(site_url):
    pass

class TestOpenWebsiteSkill(unittest.TestCase):
    """Integration tests for `OpenWebsiteSkill`."""
    def setUp(self):
        self.skill = OpenWebsiteSkill()
    
    def test_skillShouldRecognizeSentence(self):
        cmd_list = ["start", "open", "go", "go to", "take me to"]
        sentences = [cmd + " https://www.ltu.edu/" for cmd in cmd_list]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"OpenWebsiteSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    @mock.patch("webbrowser.open", side_effect=webbrowser_open)
    def test_skillShouldOpenCorrectWebsites(self, webbrowser_open_function):
        cmd_list = ["start", "open", "go", "go to", "take me to"]
        site_names_list = ['ltu website', 'ltu homepage']
        sentences = [cmd + " " + site_name for cmd in cmd_list for site_name in site_names_list]
        site_name = "the main LTU website"
        site_url = "http://www.ltu.edu"
        expected_output_speech = f"Opening {site_name}..."

        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"OpenWebsiteSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
            self.skill.execute_for_command(skill_input, mock_assistant_services)
            mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, False)
            webbrowser_open_function.assert_called()
            webbrowser_open_function.assert_called_with(site_url)