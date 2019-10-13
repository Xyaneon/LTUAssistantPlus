#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.change_assistant_voice_skill import ChangeAssistantVoiceSkill
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestChangeAssistantVoiceSkill(unittest.TestCase):
    """Unit tests for `ChangeAssistantVoiceSkill`."""
    def setUp(self):
        self.skill = ChangeAssistantVoiceSkill()
    
    def test_skillShouldRecognizeCommand(self):
        verbs = ["use"]

        for verb in verbs:
            ud = ParsedUniversalDependencies(verb=verb)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"ChangeAssistantVoiceSkill did not recognize verb='{verb}'")