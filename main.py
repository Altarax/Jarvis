import speech_recognition as sr
import pyttsx3
from gpt import get_answer_from_gpt
from global_variables import *

# GLOBAL VARIABLES
engine = None
recognizer = None

def initialize():
    global engine, recognizer
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

def recognize_voice() -> str:
    default_text = "None"

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        capted_text = recognizer.recognize_google(audio, language="fr-FR")
    except sr.UnknownValueError:
        return default_text

    if capted_text.startswith(command_prefix):
        command = capted_text[len(command_prefix):]
        command = command.strip()
        return command
    else:
        return default_text

def main_loop():
    while True:
        recognized_sentence = recognize_voice()
        if recognized_sentence == "None":
            engine.runAndWait()
            continue
        else:
            engine.say(get_answer_from_gpt(recognized_sentence))
            engine.runAndWait()

if __name__ == "__main__":
    initialize()
    main_loop()