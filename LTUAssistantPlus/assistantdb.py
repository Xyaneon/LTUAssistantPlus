#!/usr/bin/python3

import argparse
import sys

from nlp.universal_dependencies import ParsedUniversalDependencies

from skills.skill import SkillInput, Skill
from skills.open_website_skill import OpenWebsiteSkill
from skills.send_email_skill import SendEmailSkill
from skills.room_finder_skill import RoomFinderSkill
from skills.add_calendar_event_skill import AddCalendarEventSkill
from skills.tell_schedule_skill import TellScheduleSkill
from skills.tell_date_skill import TellDateSkill
from skills.tell_time_skill import TellTimeSkill
from skills.change_assistant_voice_skill import ChangeAssistantVoiceSkill
from skills.change_user_name_skill import ChangeUserNameSkill

def identify_and_run_command(ud: ParsedUniversalDependencies, verbose: bool = False) -> bool:
    """Parse the command and take an action. Returns True if the command is
    understood, and False otherwise."""
    skill_input = SkillInput(ud, verbose)

    # Print parameters for debugging purposes
    print('\tverb:           ' + (skill_input.verb if skill_input.verb is not None else "(None)"))
    print('\tverb_object:    ' + (skill_input.verb_object if skill_input.verb_object is not None else "(None)"))
    print('\talternate_noun: ' + (skill_input.alternate_noun if skill_input.alternate_noun is not None else "(None)"))
    print('\tadjective:      ' + (skill_input.adjective if skill_input.adjective is not None else "(None)"))

    available_skills = [
        OpenWebsiteSkill(),
        SendEmailSkill(),
        RoomFinderSkill(),
        AddCalendarEventSkill(),
        TellScheduleSkill(),
        TellDateSkill(),
        TellTimeSkill(),
        ChangeAssistantVoiceSkill(),
        ChangeUserNameSkill()]
    
    for available_skill in available_skills:
        if available_skill.matches_command(skill_input):
            available_skill.execute_for_command(skill_input)
            return True
    return False

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
    identify_and_run_command(ud, args.verbose)
    exit()
