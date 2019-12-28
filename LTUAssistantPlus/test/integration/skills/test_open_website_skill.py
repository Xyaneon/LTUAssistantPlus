#!/usr/bin/python3

import unittest
from unittest import mock
from unittest.mock import create_autospec, Mock, patch
import webbrowser

from services.assistant_services_base import AssistantServicesBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from skills.skill import SkillInput
from skills.open_website_skill import OpenWebsiteSkill, _SupportedWebsite
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

def webbrowser_open(site_url):
    pass

class TestOpenWebsiteSkill(unittest.TestCase):
    """Integration tests for `OpenWebsiteSkill`."""
    def setUp(self):
        self.skill = OpenWebsiteSkill()
        self.cmd_list = ["start", "open", "go to", "take me to"]
        self._supported_websites = [
            _SupportedWebsite(
                ['bannerweb', 'banner', 'registration', 'financial aid'],
                "BannerWeb",
                "https://www.ltu.edu/bannerweb"
            ),
            _SupportedWebsite(
                ['blackboard', 'bb'],
                "BlackBoard",
                "https://my.ltu.edu"
            ),
            _SupportedWebsite(
                ['library', 'ltu library'],
                "the LTU Library homepage",
                "https://www.ltu.edu/library"
            ),
            _SupportedWebsite(
                ['help desk', 'helpdesk', 'tech support', 'ehelp'],
                "the LTU eHelp homepage",
                "http://www.ltu.edu/ehelp/"
            ),
            _SupportedWebsite(
                ['password', 'mypassword'],
                "MyPassword web service",
                "https://mypassword.campus.ltu.edu/"
            ),
            _SupportedWebsite(
                ['ltu.edu', 'ltu website', 'ltu homepage', 'main ltu website'],
                "the main LTU website",
                "http://www.ltu.edu"
            ),
            _SupportedWebsite(
                ['email', 'webmail', 'mail', 'gmail'],
                "Gmail",
                "https://gmail.com"
            ),
            _SupportedWebsite(
                ['calendar', 'schedule', 'events'],
                "Google Calendar",
                "https://calendar.google.com"
            ),
            _SupportedWebsite(
                ['ltu events', 'ltu event'],
                "ltu events",
                "http://www.ltu.edu/myltu/calendar.asp"
            )
        ]
    
    def test_skillShouldRecognizeSentence(self):
        sentences = [cmd + " https://www.ltu.edu/" for cmd in self.cmd_list]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"OpenWebsiteSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    @mock.patch("webbrowser.open", side_effect=webbrowser_open)
    def test_skillShouldOpenCorrectWebsites(self, webbrowser_open_function):
        failure_count = 0
        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service
        
        for website in self._supported_websites:
            sentences = [cmd + " " + site_name for cmd in self.cmd_list for site_name in website.request_names]
            expected_output_speech = f"Opening {website.site_name}..."

            for sentence in sentences:
                ud = Parse(sentence)
                skill_input = SkillInput(sentence, ud, False)
                try:
                    self.assertTrue(
                        self.skill.matches_command(skill_input),
                        f"OpenWebsiteSkill did not recognize sentence='{sentence}'\nud: {ud}"
                    )
                    self.skill.execute_for_command(skill_input, mock_assistant_services)
                    mock_assistant_services.user_interaction_service.speak.assert_called_with(expected_output_speech, False)
                    webbrowser_open_function.assert_called_with(website.site_url)
                except AssertionError as e:
                    print(f"OpenWebsiteSkill did not recognize website name for sentence='{sentence}'\n\tud: {ud}\n{str(e)}")
                    failure_count += 1
        
        self.assertEqual(failure_count, 0, f"There were {str(failure_count)} failure(s) in this test.")