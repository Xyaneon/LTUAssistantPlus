#!/usr/bin/env python3

import listening
import speaking

def ask_question(question, also_cmd=False):
    '''Ask the user a question and return the reply as a string.'''
    speaking.speak(question, also_cmd)
    num_tries = 3
    for x in range(0, num_tries):
        (success, sentence) = listening.listen()
        if success:
            return sentence
        else:
            speaking.speak('I\'m sorry, could you repeat that?', also_cmd)
    speaking.speak('I\'m sorry, I could not understand you.', also_cmd)
    return ''