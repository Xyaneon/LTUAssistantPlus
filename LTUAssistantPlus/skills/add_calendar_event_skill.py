#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from services.calendar.calendar_event import CalendarEvent
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
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        verb_object = skill_input.dependencies.noun
        event_str = verb_object
        if event_str == 'event':
            event_sentence = services.user_interaction_service.ask_question('Okay, what is the event called?', skill_input.verbose)
            day_sentence = services.user_interaction_service.ask_question('What day will this be on?', skill_input.verbose)
            time_sentence = services.user_interaction_service.ask_question('What time will this start at?', skill_input.verbose)
            cal_event = CalendarEvent(event_sentence, day_sentence, time_sentence, '')
            services.calendar_service.add_event(cal_event)
            feedback_sentence = 'Alright, I\'m putting down ' + str(cal_event) + '.'
            services.user_interaction_service.speak(feedback_sentence, skill_input.verbose)
        else:
            services.user_interaction_service.speak('Sorry, I am unable to help you schedule this right now.', skill_input.verbose)
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass