#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.send_email_skill import SendEmailSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestSendEmailSkill(unittest.TestCase):
    """Unit tests for `SendEmailSkill`."""
    def setUp(self):
        self.skill = SendEmailSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["email", "compose", "compose to", "send", "send to", "write", "write to"]

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"SendEmailSkill did not recognize verb='{verb}'")