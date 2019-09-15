#!/usr/bin/python3

import listening
import speaking
from typing import Tuple

def ask_question(question, also_cmd=False):
    """Ask the user a question and return the reply as a string."""
    speaking.speak(question, also_cmd)
    num_tries = 3
    for _ in range(0, num_tries):
        (success, sentence) = listening.listen()
        if success:
            return sentence
        else:
            speaking.speak('I\'m sorry, could you repeat that?', also_cmd)
    speaking.speak('I\'m sorry, I could not understand you.', also_cmd)
    return ''

def greet_user(username: str):
    """Greets the user and asks how we can help them."""
    greeting_str = f"Hi {username}! What can I help you with?"
    speaking.speak(greeting_str, True)

def greet_user_and_ask_for_command(username: str) -> Tuple[bool, str]:
    """Greets the user, asks how we can help them, and returns the response as
    a tuple indicating whether listening was successful and what the user said.
    """
    greet_user(username)
    return listening.listen()

def tell_user_command_was_not_understood():
    """Tells the user their command was not understood."""
    speaking.speak("Sorry, I don't understand what you want.", True)

def tell_user_could_not_be_heard():
    """Tells the user they could not be heard."""
    speaking.speak("Sorry, I wasn't able to hear you.", True)