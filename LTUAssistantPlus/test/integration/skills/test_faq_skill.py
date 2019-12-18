#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.faq_skill import FAQSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

class TestFAQSkill(unittest.TestCase):
    """Integration tests for `FAQSkill`."""
    def setUp(self):
        self.skill = FAQSkill()
    
    def test_skillShouldRecognizeStaffSentences(self):
        sentences = ["who is the associate dean of the Mathematics and Computer Science Department",
                     "who is the department chair of the Mathematics and Computer Science Department"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"FAQSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
    
    def test_skillShouldRecognizeCurriculumSentences(self):
        sentences = ["What concentrations are available for a Bachelor’s of Science in Computer Science",
                     "What courses are available to take in the freshman year for a Bachelor’s of Science in Computer Science"]
        
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            self.assertTrue(
                self.skill.matches_command(skill_input),
                f"FAQSkill did not recognize sentence='{sentence}'\nud: {ud}"
            )
        pass