#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.open_website_skill import OpenWebsiteSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestOpenWebsiteSkill(unittest.TestCase):
    """Integration tests for `OpenWebsiteSkill`."""
    def setUp(self):
        self.skill = OpenWebsiteSkill()
    
    def test_skillShouldRecognizeSentence(self):
        cmd_list = ["start", "open", "go", "go to", "take me to"]
        sentences = [cmd + " https://www.ltu.edu/" for cmd in cmd_list]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"OpenWebsiteSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )