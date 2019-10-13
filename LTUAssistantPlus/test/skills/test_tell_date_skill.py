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
        verbs = ["what is", "tell"]
        nouns = ["date", "day"]

        for verb in verbs:
            for noun in nouns:
                ud = ParsedUniversalDependencies(verb=verb, noun=noun)
                skill_input = SkillInput(ud, False)
                self.assertTrue(
                    self.skill.matches_command(skill_input),
                    f"TellDateSkill did not recognize verb='{verb}' and noun='{noun}'")