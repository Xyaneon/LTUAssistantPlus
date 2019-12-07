#!/usr/bin/python3

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from .skill import SkillInput, Skill

class RoomFinderSkill(Skill):
    """Lets the assistant find LTU rooms for the user when given a room number."""

    def __init__(self):
        """Initializes a new instance of the RoomFinderSkill class."""
        self._cmd_list = ['find', 'where is']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        room_str = verb_object
        finder_message = ''
        if room_str:
            words = room_str.split()
            if words[0] == "room":
                words.remove("room")
            if not len(words) or len(words[0]) not in range(4, 6):
                finder_message = 'Sorry, but I don\'t think you told me which room you want.'
            # TODO: Use a regular expression for better room number validity
            else:
                print(words)
                room_letter = words[0][0].upper()
                room_floor = words[0][1]
                building_dict = {'A': 'Architecture Building',
                                'B': 'Business Services Building',
                                'C': 'A. Alfred Taubman Student Services Center',
                                'D': 'Art and Design Center',
                                'F': 'CIMR Building',
                                'E': 'Engineering Building',
                                'R': 'Ridler Field House and Applied Research Center',
                                'M': 'Wayne H. Buell Management Building',
                                'S': 'Arts and Sciences Building',
                                'T': 'University Technology and Learning Center'
                                }
                if room_letter in building_dict.keys():
                    building = building_dict[room_letter]
                else:
                    building = ''

                if building != '':
                    finder_message = 'Your room is in the ' + building + ' on floor ' + room_floor + '.'
                else:
                    finder_message = 'Sorry, I don\'t know which building that is.'
        else:
            finder_message = 'Sorry, but I don\'t think you told me which room you want.'
        user_interaction_service.speak(finder_message, skill_input.verbose)
    
    def perform_setup(self):
        """Executes any setup work necessary for this skill before it can be used."""
        pass