import pywhatkit
import wikipedia
import pyjokes


def run_alexa():
    command = ''
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
    elif 'joke' in command:
        pyjokes.get_joke()
