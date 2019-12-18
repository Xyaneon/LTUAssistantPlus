#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_schedule_skill import TellScheduleSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellScheduleSkill(unittest.TestCase):
    """Integration tests for `TellScheduleSkill`."""
    def setUp(self):
        self.skill = TellScheduleSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["tell me my schedule",
                     "what is my schedule"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"TellScheduleSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )