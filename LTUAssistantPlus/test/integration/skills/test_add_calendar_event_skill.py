#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.add_calendar_event_skill import AddCalendarEventSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestAddCalendarEventSkill(unittest.TestCase):
    """Integration tests for `AddCalendarEventSkill`."""
    def setUp(self):
        self.skill = AddCalendarEventSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["plan an event",
                     "remind me about an event",
                     "schedule an event"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"AddCalendarEventSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    def test_skillShouldNotRecognizeSentencesAskingAboutCurrentSchedule(self):
        sentences = ["tell me my schedule",
                     "what is my schedule"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertFalse(
                self.skill.matches_command(skill_input),
                f"AddCalendarEventSkill recognized sentence='{sentence}'\nud: {ud}"
            )