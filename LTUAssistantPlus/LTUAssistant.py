#!/usr/bin/python3

import argparse
import user_interface.interactions
import user_interface.listening
import re
import sys
import settings
import user_interface.speaking
import assistantdb
from nlp.natural_language_processing import Parse

def process_command(optional_message: str = None):
    """Processes a command, either supplied as a parameter or obtained from
    user interaction."""
    if optional_message:
        sentence = optional_message
        print(f"Text input provided: {optional_message}")
    else:
        (success, sentence) = user_interface.interactions.greet_user_and_ask_for_command(settings.username.capitalize())
        if not success:
            user_interface.interactions.tell_user_could_not_be_heard()
            return
    ud = Parse(sentence)
    if not assistantdb.identify_and_run_command(ud):
        user_interface.interactions.tell_user_command_was_not_understood()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text-only-mode',
                        help='make all user interaction happen in the terminal',
                        action='store_true')
    parser.add_argument('-c', '--command-string',
                        help='user\'s initial command text in string form',
                        type=str)
    args = parser.parse_args()
    
    if args.text_only_mode:
        user_interface.listening.text_only_mode = True
        user_interface.speaking.text_only_mode = True
    if args.command_string:
        process_command(args.command_string)
    else:
        process_command()
