#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_time_skill import TellTimeSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellTimeSkill(unittest.TestCase):
    """Unit tests for `TellTimeSkill`."""
    def setUp(self):
        self.skill = TellTimeSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["what is", "tell"]
        nouns = ["time"]

        for verb in verbs:
            for noun in nouns:
                ud = ParsedUniversalDependencies(verb=verb, noun=noun)
                skill_input = SkillInput(ud, False)
                self.assertTrue(
                    self.skill.matches_command(skill_input),
                    f"TellTimeSkill did not recognize verb='{verb}' and noun='{noun}'")