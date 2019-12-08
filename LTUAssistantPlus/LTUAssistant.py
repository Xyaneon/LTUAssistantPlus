#!/usr/bin/python3

import argparse
import re
import sys
import skill_selection
from nlp.natural_language_processing import Parse
from services.assistant_services import AssistantServices

def process_command(services: AssistantServices, optional_message: str = None):
    """Processes a command, either supplied as a parameter or obtained from
    user interaction."""
    if optional_message:
        sentence = optional_message
        print(f"Text input provided: {optional_message}")
    else:
        (success, sentence) = services.user_interaction_service.greet_user_and_ask_for_command(services.settings_service.username.capitalize())
        if not success:
            services.user_interaction_service.tell_user_could_not_be_heard()
            return
    ud = Parse(sentence)
    if not skill_selection.identify_and_run_command(ud, services):
        services.user_interaction_service.tell_user_command_was_not_understood()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text-only-mode',
                        help='make all user interaction happen in the terminal',
                        action='store_true')
    parser.add_argument('-c', '--command-string',
                        help='user\'s initial command text in string form',
                        type=str)
    args = parser.parse_args()

    services = AssistantServices(args.text_only_mode)

    if args.command_string:
        process_command(services, args.command_string)
    else:
        process_command(services)
