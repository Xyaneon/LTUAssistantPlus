#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.send_email_skill import SendEmailSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

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