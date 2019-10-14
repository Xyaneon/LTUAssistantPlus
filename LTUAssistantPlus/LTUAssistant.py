#!/usr/bin/python3

import argparse
import re
import sys
import settings
import assistantdb
from nlp.natural_language_processing import Parse
from user_interface.listening_service_base import ListeningServiceBase
from user_interface.listening_service import ListeningService
from user_interface.speaking_service_base import SpeakingServiceBase
from user_interface.speaking_service import SpeakingService
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from user_interface.user_interaction_service import UserInteractionService

def process_command(interaction_service: UserInteractionServiceBase, optional_message: str = None):
    """Processes a command, either supplied as a parameter or obtained from
    user interaction."""
    if optional_message:
        sentence = optional_message
        print(f"Text input provided: {optional_message}")
    else:
        (success, sentence) = interaction_service.greet_user_and_ask_for_command(settings.username.capitalize())
        if not success:
            interaction_service.tell_user_could_not_be_heard(speak_service)
            return
    ud = Parse(sentence)
    if not assistantdb.identify_and_run_command(ud, interaction_service):
        interaction_service.tell_user_command_was_not_understood(speak_service)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text-only-mode',
                        help='make all user interaction happen in the terminal',
                        action='store_true')
    parser.add_argument('-c', '--command-string',
                        help='user\'s initial command text in string form',
                        type=str)
    args = parser.parse_args()
    
    speak_service = SpeakingService(args.text_only_mode)
    listen_service = ListeningService(args.text_only_mode)
    interaction_service = UserInteractionService(speak_service, listen_service)

    if args.command_string:
        process_command(interaction_service, args.command_string)
    else:
        process_command(interaction_service)
