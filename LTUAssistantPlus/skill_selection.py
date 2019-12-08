#!/usr/bin/python3

import argparse
import sys

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase

from skills.skill import SkillInput, Skill
from skills import available_skills

from typing import Optional

def identify_and_run_command(ud: ParsedUniversalDependencies, services: AssistantServicesBase, verbose: bool = False) -> bool:
    """Parse the command and take an action. Returns True if the command is
    understood, and False otherwise."""
    skill_input = SkillInput(ud, verbose)

    # Print parameters for debugging purposes
    print('\tverb:           ' + (skill_input.verb if skill_input.verb is not None else "(None)"))
    print('\tverb_object:    ' + (skill_input.verb_object if skill_input.verb_object is not None else "(None)"))
    print('\talternate_noun: ' + (skill_input.alternate_noun if skill_input.alternate_noun is not None else "(None)"))
    print('\tadjective:      ' + (skill_input.adjective if skill_input.adjective is not None else "(None)"))

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('verb', type=str, help='Assistant database command.')
    parser.add_argument('verb_object', type=str, help='Object passed to command.')
    parser.add_argument('-v', '--verbose',
                        help='Explain what action is being taken.',
                        action='store_true')
    args = parser.parse_args()

    if args.verbose:
        print(sys.version)
    ud = ParsedUniversalDependencies(verb = args.verb, noun = args.verb_object)
    identify_and_run_command(ud, None, args.verbose)
    exit()
