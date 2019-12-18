#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.change_assistant_voice_skill import ChangeAssistantVoiceSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestChangeAssistantVoiceSkill(unittest.TestCase):
    """Integration tests for `ChangeAssistantVoiceSkill`."""
    def setUp(self):
        self.skill = ChangeAssistantVoiceSkill()
    
    def test_skillShouldRecognizeSentence(self):
        sentences = ["use a male voice",
                     "use a female voice"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"ChangeAssistantVoiceSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )