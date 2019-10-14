#!/usr/bin/python3

import calendardb
import user_interface.interactions

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.speaking_service_base import SpeakingServiceBase
from .skill import SkillInput, Skill

class AddCalendarEventSkill(Skill):
    """Lets the assistant schedule a calendar event for the user."""

    def __init__(self):
        """Initializes a new instance of the AddCalendarEventSkill class."""
        self._cmd_list = ['schedule', 'remind', 'remind about', 'plan']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, speak_service: SpeakingServiceBase):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        event_str = verb_object
        if event_str == 'event':
            event_sentence = user_interface.interactions.ask_question('Okay, what is the event called?', speak_service, skill_input.verbose)
            day_sentence = user_interface.interactions.ask_question('What day will this be on?', speak_service, skill_input.verbose)
            time_sentence = user_interface.interactions.ask_question('What time will this start at?', speak_service, skill_input.verbose)
            cal_event = calendardb.CalendarEvent(event_sentence, day_sentence, time_sentence, '')
            calendardb.add_event(cal_event)
            feedback_sentence = 'Alright, I\'m putting down ' + str(cal_event) + '.'
            speak_service.speak(feedback_sentence, skill_input.verbose)
        else:
            speak_service.speak('Sorry, I am unable to help you schedule this right now.', skill_input.verbose)