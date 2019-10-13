#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_schedule_skill import TellScheduleSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellScheduleSkill(unittest.TestCase):
    """Unit tests for `TellScheduleSkill`."""
    def setUp(self):
        self.skill = TellScheduleSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["what is", "tell"]
        nouns = ["schedule"]

        for verb in verbs:
            for noun in nouns:
                ud = ParsedUniversalDependencies(verb=verb, noun=noun)
                skill_input = SkillInput(ud, False)
                self.assertTrue(
                    self.skill.matches_command(skill_input),
                    f"TellScheduleSkill did not recognize verb='{verb}' and noun='{noun}'")