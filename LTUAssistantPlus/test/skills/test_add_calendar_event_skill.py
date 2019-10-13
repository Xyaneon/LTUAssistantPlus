#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.add_calendar_event_skill import AddCalendarEventSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestAddCalendarEventSkill(unittest.TestCase):
    """Unit tests for `AddCalendarEventSkill`."""
    def setUp(self):
        self.skill = AddCalendarEventSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["schedule", "remind", "remind about", "plan"]

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"AddCalendarEventSkill did not recognize verb='{verb}'")