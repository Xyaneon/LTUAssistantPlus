#!/usr/bin/python3

import unittest

from skills.skill import SkillInput
from skills.faq_skill import FAQSkill
from nlp.natural_language_processing import Parse
from nlp.universal_dependencies import ParsedUniversalDependencies

from typing import List

class TestFAQSkill(unittest.TestCase):
    """Integration tests for `FAQSkill`."""
    def setUp(self):
        self.skill = FAQSkill()
    
    def test_skillShouldRecognizeStaffSentences(self):
        sentences = ["who is the associate dean of the Mathematics and Computer Science Department",
                     "who is the department chair of the Mathematics and Computer Science Department"]
        self._check_matching_sentences(sentences)
    
    def test_skillShouldRecognizeCurriculumSentences(self):
        sentences = ["What concentrations are available for a Bachelor’s of Science in Computer Science",
                     "What courses are available to take in the freshman year for a Bachelor’s of Science in Computer Science"]
        self._check_matching_sentences(sentences)

    def _check_matching_sentences(self, sentences: List[str]):
        failures = []
        for sentence in sentences:
            ud = Parse(sentence)
            skill_input = SkillInput(ud, False)
            try:
                self.assertTrue(
                    self.skill.matches_command(skill_input),
                    f"FAQSkill did not recognize sentence='{sentence}'\n\tud: {ud}"
                )
            except AssertionError:
                failures.append(f"FAQSkill did not recognize sentence='{sentence}'\n  ud: {ud}")
        self.assertTrue(failures == [], "One or more sentences were not recognized:\n" + "\n".join(failures))