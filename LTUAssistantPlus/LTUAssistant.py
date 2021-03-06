#!/usr/bin/python3

import argparse

import skill_selection
from nlp.natural_language_processing import Parse
from services.assistant_services import AssistantServices
from services.assistant_services_base import AssistantServicesBase
from skills import init_skills


def process_command(services: AssistantServicesBase, optional_message: str = None, verbose: bool = False):
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
    if not skill_selection.identify_and_run_command(sentence, ud, services, verbose):
        services.user_interaction_service.tell_user_command_was_not_understood()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text-only-mode',
                        help='make all user interaction happen in the terminal',
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help='show verbose output in the terminal',
                        action='store_true')
    parser.add_argument('-c', '--command-string',
                        help='user\'s initial command text in string form',
                        type=str)
    args = parser.parse_args()

    services = AssistantServices(text_only_mode=args.text_only_mode)
    init_skills(services)

    if args.command_string:
        process_command(services, args.command_string, args.verbose)
    else:
        process_command(services)
