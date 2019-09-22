#!/usr/bin/python3

import argparse
import sys

from nlp.universal_dependencies import ParsedUniversalDependencies

from skills.skill import Skill
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
    verb = (ud.verb or None) and ud.verb.lower()
    verb_object = ud.noun
    alternate_noun = ud.noun # TODO: Actually get the correct alternate noun.
    adjective = (ud.adj or None) and ud.adj.lower()
    # Print parameters for debugging purposes
    print('\tverb:           ' + (verb if verb is not None else "(None)"))
    print('\tverb_object:    ' + (verb_object if verb_object is not None else "(None)"))
    print('\talternate_noun: ' + (alternate_noun if alternate_noun is not None else "(None)"))
    print('\tadjective:      ' + (adjective if adjective is not None else "(None)"))

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
        if available_skill.matches_command(ud):
            available_skill.execute_for_command(ud, verbose)
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
