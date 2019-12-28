#!/usr/bin/python3

import argparse
import sys

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from skills.skill import SkillInput, Skill
from skills import available_skills

from typing import Optional


def identify_and_run_command(sentence: str,
                             ud: ParsedUniversalDependencies,
                             services: AssistantServicesBase,
                             verbose: bool = False) -> bool:
    """Parse the command and take an action. Returns True if the command is
    understood, and False otherwise."""
    skill_input = SkillInput(sentence, ud, verbose)

    # Print parameters for debugging purposes
    print('  * Universal dependencies:\n      ' + (str(skill_input.dependencies) if skill_input.dependencies is not None else "(None)"))
    print('  * verb:           ' + (skill_input.verb if skill_input.verb is not None else "(None)"))
    print('  * verb_object:    ' + (skill_input.verb_object if skill_input.verb_object is not None else "(None)"))
    print('  * alternate_noun: ' + (skill_input.alternate_noun if skill_input.alternate_noun is not None else "(None)"))
    print('  * adjective:      ' + (skill_input.adjective if skill_input.adjective is not None else "(None)"))

    skill = _select_skill_for_input(skill_input)
    if skill is not None:
        skill.execute_for_command(skill_input, services)
        return True
    return False


def _select_skill_for_input(skill_input: SkillInput) -> Optional[Skill]:
    """
    Selects a `Skill` which can process the given `SkillInput` and returns it.
    Alternatively, `None` is returned if there is no suitable `Skill` found.
    """
    for available_skill in available_skills:
        if available_skill.matches_command(skill_input):
            return available_skill
    return None
