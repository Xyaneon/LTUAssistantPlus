#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.tell_date_skill import TellDateSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestTellDateSkill(unittest.TestCase):
    """Integration tests for `TellDateSkill`."""
    def setUp(self):
        self.skill = TellDateSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["tell the date",
                     "tell me the date",
                     "tell the current date",
                     "tell me the current date"
                     "what is the date",
                     "what is the current date"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"TellDateSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )