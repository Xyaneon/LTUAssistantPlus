#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.change_user_name_skill import ChangeUserNameSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestChangeUserNameSkill(unittest.TestCase):
    """Unit tests for `ChangeUserNameSkill`."""
    def setUp(self):
        self.skill = ChangeUserNameSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["call"]

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"ChangeUserNameSkill did not recognize verb='{verb}'")