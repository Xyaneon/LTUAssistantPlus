#!/usr/bin/python3

import re
import traceback

from nlp.universal_dependencies import ParsedUniversalDependencies
from services.assistant_services_base import AssistantServicesBase
from .skill import SkillInput, Skill

from typing import Tuple

class RoomFinderSkill(Skill):
    """Lets the assistant find LTU rooms for the user when given a room number."""

    def __init__(self):
        """Initializes a new instance of the RoomFinderSkill class."""
        self._building_dict = {
            'A': 'Architecture Building',
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

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        deps = skill_input.dependencies
        return deps.verb == "find" or (deps.adv == "where" and deps.aux == "be")
    
    def execute_for_command(self, skill_input: SkillInput, services: AssistantServicesBase):
        """Executes this skill on the given command input."""
        try:
            building_and_floor = self._convert_room_number_to_building_and_floor(skill_input.dependencies.propn)
            building = building_and_floor[0]
            floor = building_and_floor[1]
            finder_message = f"Your room is in the {building} on floor {floor}."
        except Exception:
            finder_message = "Sorry, I don't think you provided me with a valid room number."
        services.user_interaction_service.speak(finder_message, skill_input.verbose)
    
    def perform_setup(self, services):
        """Executes any setup work necessary for this skill before it can be used."""
        pass

    def _convert_room_number_to_building_and_floor(self, room_number: str) -> Tuple[str, int]:
        """Converts a room number (for example, A101) into a building name and floor number."""
        pattern = r"([A-z])0*([\d])\d*"
        try:
            match = re.match(pattern, room_number)
            room_letter = match.group(1).upper()
            floor_number = int(match.group(2))
            
            if room_letter in self._building_dict.keys():
                building = self._building_dict[room_letter]
            else:
                raise RuntimeError(f"Unidentified room letter '{room_letter}'.")
            return (building, floor_number)
        except Exception as e:
            raise ValueError("Invalid room number string.") from e