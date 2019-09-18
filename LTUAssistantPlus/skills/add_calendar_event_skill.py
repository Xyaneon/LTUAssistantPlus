#!/usr/bin/python3

import calendardb
import interactions
import speaking

from nlp.universal_dependencies import ParsedUniversalDependencies
from .skill import Skill

class AddCalendarEventSkill(Skill):
    """Lets the assistant schedule a calendar event for the user."""

    def __init__(self):
        """Initializes a new instance of the AddCalendarEventSkill class."""
        self._cmd_list = ['schedule', 'remind', 'remind about', 'plan']

    def matches_command(self, command_input: ParsedUniversalDependencies) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (command_input.verb or None) and command_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, command_input: ParsedUniversalDependencies, verbose: bool):
        """Executes this skill on the given command input."""
        verb_object = command_input.noun
        event_str = verb_object
        if event_str == 'event':
            event_sentence = interactions.ask_question('Okay, what is the event called?', verbose)
            day_sentence = interactions.ask_question('What day will this be on?', verbose)
            time_sentence = interactions.ask_question('What time will this start at?', verbose)
            cal_event = calendardb.CalendarEvent(event_sentence, day_sentence, time_sentence, '')
            calendardb.add_event(cal_event)
            feedback_sentence = 'Alright, I\'m putting down ' + str(cal_event) + '.'
            speaking.speak(feedback_sentence, verbose)
        else:
            speaking.speak('Sorry, I am unable to help you schedule this right now.', verbose)