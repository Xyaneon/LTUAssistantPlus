#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services import AssistantServices
from .skill import SkillInput, Skill

class TellScheduleSkill(Skill):
    """Lets the assistant tell the user their schedule."""

    def __init__(self):
        """Initializes a new instance of the TellScheduleSkill class."""
        self._cmd_list = ['what is', 'tell']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        verb_object = (skill_input.verb_object or None) and skill_input.verb_object.lower()
        return verb in self._cmd_list and verb_object == "schedule"
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServices):
        """Executes this skill on the given command input."""
        event_list = services.calendar_service.get_todays_events()
        if len(event_list) < 1:
            output_str = 'There are no events currently scheduled.'
        elif len(event_list) == 1:
            output_str = ' '.join(['You only have', event_list[0].event_str, 'at',
                                event_list[0].start_time_str]) + '.'
        elif len(event_list) == 2:
            output_str = ' '.join(['You have', event_list[0].event_str, 'at',
                                event_list[0].start_time_str, 'and',
                                event_list[1].event_str, 'at',
                                event_list[1].start_time_str]) + '.'
        else:
            # 3 or more events
            output_str = 'You have '
            for event in event_list[:-1]:
                output_str += ' '.join([event.event_str, 'at',
                                        event.start_time_str]) + ', '
            output_str += ' '.join(['and', event_list[-1].event_str, 'at',
                                    event_list[-1].start_time_str]) + '.'
        services.user_interaction_service.speak(output_str, skill_input.verbose)
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass