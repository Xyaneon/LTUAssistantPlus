#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import notifications
import settings
import subprocess

text_only_mode = False

def speak(message, also_cmd=False):
    '''Speak the given message using the text-to-speech backend.'''
    if also_cmd or text_only_mode:
        print(message)
    notifications.show_notification(message, also_cmd)
    if not text_only_mode:
        if settings.voice == 'female':
            # Speak using a female voice
            subprocess.call('espeak -v+f1 "' + message + '"', shell=True)
        else:
            # Default to male voice
            subprocess.call('espeak "' + message + '"', shell=True)