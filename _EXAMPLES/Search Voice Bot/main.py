# chrome version: 110.0.5481.178
# pip install pyaudio selenium SpeechRecognition

import speech_recognition as sr
from selenium import webdriver


class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()

                    print(command)

            except sr.UnknownValueError:
                pass


listener = Voice()
