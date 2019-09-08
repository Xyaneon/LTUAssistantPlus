#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import notifications
import settings
import speech_recognition as sr
import subprocess

text_only_mode = False

def listen():
    '''Gets a command from the user, either via the microphone or command line
    if text-only mode was specified.'''
    if text_only_mode:
        ret = input('\t> ')
        return True, ret
    else:
        # obtain audio from the microphone
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

if __name__ == '__main__':
    (success, error) = listen()
    if not success:
        print(error)
