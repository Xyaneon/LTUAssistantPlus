#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import notifications
import platform
import settings
import subprocess

platform_string = platform.system()
if platform_string == "Windows":
    from win32com.client import Dispatch
    winspeak = Dispatch("SAPI.SpVoice")

text_only_mode = False

def speak(message, also_cmd=False):
    '''Speak the given message using the text-to-speech backend.'''
    if also_cmd or text_only_mode:
        __say_in_terminal(message)
    __say_in_notification(message, also_cmd)
    if not text_only_mode:
        __say_via_audio(message)

def __say_in_terminal(message):
    '''Shows the spoken message in the CLI.'''
    print(message)

def __say_in_notification(message, also_cmd):
    '''Shows the spoken message in a system notification.'''
    notifications.show_notification(message, also_cmd)

def __say_via_audio(message):
    '''Says the spoken message via system audio.'''
    if platform_string == "Linux":
        if settings.voice == 'female':
            # Speak using a female voice
            subprocess.call('espeak -v+f1 "' + message + '"', shell=True)
        else:
            # Default to male voice
            subprocess.call('espeak "' + message + '"', shell=True)
    elif platform_string == "Windows":
        # TODO: Respect voice configuration settings.
        winspeak.speak(message)

if __name__ == "__main__":
    speak("This is a test message from LTU Assistant.", True)