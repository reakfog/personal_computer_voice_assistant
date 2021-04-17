import sys  
sys.path = ['', '..'] + sys.path[1:]

from termcolor import colored
from assistance_bot import settings, core

def setup_assistant_voice(engine, assistant_obj):
    """
    Setting the default voice (the index may vary depending
    on the settings of the operating system)
    """
    voices = engine.getProperty("voices")
    if assistant_obj == 'en':
        assistant_obj.recognition_language = 'en-US'
        if assistant_obj.sex == 'female':
            # Microsoft Zira Desktop - English (United States)
            engine.setProperty('voice', voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            engine.setProperty('voice', voices[2].id)
    else:
        assistant_obj.recognition_language = 'ru-RU'
        # Microsoft Irina Desktop - Russian
        engine.setProperty('voice', voices[0].id)


def play_voice_assistant_speech(engine, text):
    """
    Play voice assistant speech answers or return data in text format
    """
    if settings.VOICE:
        engine.say(text)
        engine.runAndWait()
    print(core.assistant.name, ': ', colored(text, 'yellow'))
