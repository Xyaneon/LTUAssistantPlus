#!/usr/bin/python3

# NOTE: This module requires PyAudio because it uses the Microphone class.

import settings
import speech_recognition as sr
import subprocess

from typing import Tuple

text_only_mode = False

def listen() -> Tuple[bool, str]:
    '''Gets a command from the user, either via the microphone or command line
    if text-only mode was specified.'''
    if text_only_mode:
        return __listen_from_terminal()
    else:
        return __listen_from_microphone()

def __listen_from_microphone() -> Tuple[bool, str]:
    '''Gets a command from the user via the microphone.'''
    r = sr.Recognizer()
    ret = ""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        # Timeout after 10 seconds, in case this doesn't work
        audio = r.listen(source, 10)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Sending recorded speech to Google...")
        sentence = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said '" + sentence + "'.")
        return True, sentence
    except sr.UnknownValueError:
        ret = "Google Speech Recognition could not understand audio."
    except sr.RequestError:
        ret = "Could not request results from Google Speech Recognition."
    return False, ret

def __listen_from_terminal() -> Tuple[bool, str]:
    '''Gets a command from the user via the CLI.'''
    ret = input('\t> ')
    return True, ret

if __name__ == '__main__':
    (success, error) = listen()
    if not success:
        print(error)
