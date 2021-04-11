import sys  
sys.path = ['', '..'] + sys.path[1:]

import random
from assistance_bot import core
from . import voice_processing


def play_error(*args: tuple):
    """
    Playing a error
    """
    pass

def play_greetings(*args: tuple):
    """
    Playing a random greeting speech
    """
    owner = core.owner.name
    greetings = [
        f'Hello, {owner}! How can I help you today?',
        f'Good day to you {owner}! How can I help you today?']
    text = random.choice(greetings)
    voice_processing.play_voice_assistant_speech(core.ttsEngine, text)


def play_farewell_and_quit(*args: tuple):
    """
    Play the farewell speech and exit
    """
    owner = core.owner.name
    farewells = [
        f'Goodbye, {owner}! Have a nice day!',
        f'See you soon, {owner}!']
    text = random.choice(farewells)
    voice_processing.play_voice_assistant_speech(core.ttsEngine, text)
    core.ttsEngine.stop()
    quit()
