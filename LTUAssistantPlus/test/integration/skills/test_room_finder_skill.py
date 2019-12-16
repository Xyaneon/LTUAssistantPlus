#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.room_finder_skill import RoomFinderSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestRoomFinderSkill(unittest.TestCase):
    """Integration tests for `RoomFinderSkill`."""
    def setUp(self):
        self.skill = RoomFinderSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["find room A101",
                     "where is room A101"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"RoomFinderSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )