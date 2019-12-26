#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.room_finder_skill import RoomFinderSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestRoomFinderSkill(unittest.TestCase):
    """Unit tests for `RoomFinderSkill`."""
    def setUp(self):
        self.skill = RoomFinderSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["find"] # TODO: Add entry for "where is"

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"RoomFinderSkill did not recognize verb='{verb}'")