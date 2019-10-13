#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.open_website_skill import OpenWebsiteSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestOpenWebsiteSkill(unittest.TestCase):
    """Unit tests for `OpenWebsiteSkill`."""
    def setUp(self):
        self.skill = OpenWebsiteSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["start", "open", "go", "go to", "browse", "browse to", "launch", "take to", "show"]

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"OpenWebsiteSkill did not recognize verb='{verb}'")