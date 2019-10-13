#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_date_skill import TellDateSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellDateSkill(unittest.TestCase):
    """Unit tests for `TellDateSkill`."""
    def setUp(self):
        self.skill = TellDateSkill()
    
    def test_skillShouldRecognizeCommand(self):
        ud = ParsedUniversalDependencies(verb="what is", noun="date")
        skill_input = SkillInput(ud, False)
        self.assertTrue(self.skill.matches_command(skill_input))