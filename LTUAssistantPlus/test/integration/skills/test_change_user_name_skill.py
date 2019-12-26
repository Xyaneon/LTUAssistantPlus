#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.change_user_name_skill import ChangeUserNameSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestChangeUserNameSkill(unittest.TestCase):
    """Integration tests for `ChangeUserNameSkill`."""
    def setUp(self):
        self.skill = ChangeUserNameSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["call me Bob"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"ChangeUserNameSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )