#!/usr/bin/python3

import unittest
from unittest import mock
from unittest.mock import create_autospec, Mock, patch
import webbrowser

from services.assistant_services_base import AssistantServicesBase
from services.user_interface.user_interaction_service_base import UserInteractionServiceBase
from skills.skill import SkillInput
from skills.send_email_skill import SendEmailSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

def webbrowser_open(site_url):
    pass

class TestSendEmailSkill(unittest.TestCase):
    """Integration tests for `SendEmailSkill`."""
    def setUp(self):
        self.skill = SendEmailSkill()
    
    def test_skillShouldRecognizeSentenceWithoutRecipient(self):
        sentences = ["compose an email",
                     "send an email",
                     "write an email"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"SendEmailSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    def test_skillShouldRecognizeSentenceWithRecipient(self):
        sentences = ["compose an email to example@example.com",
                     "email example@example.com",
                     "send an email to example@example.com",
                     "write an email to example@example.com"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"SendEmailSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    @mock.patch("webbrowser.open", side_effect=webbrowser_open)
    def test_skillShouldOpenGmailWithoutRecipient(self, webbrowser_open_function):
        sentences = ["compose an email",
                     "send an email",
                     "write an email"]
        expected_url = "https://mail.google.com/mail/u/0/#compose"

        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"SendEmailSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
            self.skill.execute_for_command(skill_input, mock_assistant_services)
            webbrowser_open_function.assert_called_with(expected_url)
    
    @mock.patch("webbrowser.open", side_effect=webbrowser_open)
    def test_skillShouldOpenMailToWithRecipient(self, webbrowser_open_function):
        sentences = ["compose an email to example@example.com",
                     "email example@example.com",
                     "send an email to example@example.com",
                     "write an email to example@example.com"]
        expected_url = "mailto:example@example.com"

        mock_user_interaction_service = create_autospec(spec=UserInteractionServiceBase)
        mock_assistant_services = create_autospec(spec=AssistantServicesBase)
        mock_assistant_services.user_interaction_service.return_value = mock_user_interaction_service
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"SendEmailSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
            self.skill.execute_for_command(skill_input, mock_assistant_services)
            webbrowser_open_function.assert_called_with(expected_url)