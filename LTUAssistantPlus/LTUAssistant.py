#!/usr/bin/python3

import argparse

import skill_selection
from nlp.natural_language_processing import Parse
from services.assistant_services import AssistantServices
from services.assistant_services_base import AssistantServicesBase
from skills import init_skills


def process_command(services: AssistantServicesBase, optional_message: str = None):
    """Processes a command, either supplied as a parameter or obtained from
    user interaction."""
    if optional_message:
        sentence = optional_message
        print(f"Text input provided: {optional_message}")
    else:
        (success, sentence) = services.user_interaction_service.greet_user_and_ask_for_command(
            services.settings_service.username.capitalize())
        if not success:
            services.user_interaction_service.tell_user_could_not_be_heard()
            return
    ud = Parse(sentence)
    if not skill_selection.identify_and_run_command(ud, services):
        services.user_interaction_service.tell_user_command_was_not_understood()

from getResult import main

if __name__ == "__main__":
    main()
