#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_time_skill import TellTimeSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellTimeSkill(unittest.TestCase):
    """Integration tests for `TellTimeSkill`."""
    def setUp(self):
        self.skill = TellTimeSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["tell the time",
                     "tell me the time",
                     "tell the current time",
                     "tell me the current time"
                     "what is the time",
                     "what is the current time"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(sentence, ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"TellTimeSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )