import sys  
sys.path = ['', '..'] + sys.path[1:]

import random
import webbrowser
from googlesearch import search
from assistance_bot import core
from assistance_bot import settings
from .voice_processing.speaking import play_voice_assistant_speech


def play_error(*args: tuple) -> None:
    """Playing an error
    """
    pass


def play_greetings(*args: tuple) -> None:
    """Playing a random greeting speech
    """
    owner = core.owner.name
    phrases = [
        f'Hello, {owner}! How can I help you today?',
        f'Good day to you {owner}! How can I help you today?']
    text = random.choice(phrases)
    play_voice_assistant_speech(core.ttsEngine, text)


def play_goodbye_and_quit(*args: tuple) -> None:
    """Play the farewell speech and exit
    """
    owner = core.owner.name
    phrases = [
        f'Goodbye, {owner}! Have a nice day!',
        f'See you soon, {owner}!']
    text = random.choice(phrases)
    play_voice_assistant_speech(core.ttsEngine, text)
    core.ttsEngine.stop()
    quit()


def search_for_term_on_google(*args: tuple) -> None:
    """Google search with automatic link opening
    """
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    # alternative search with automatic opening of links to results
    search_results = []
    try:
        for _ in search(
            search_term, # what to look for
            tld='com', # top-level domain
            lang=settings.ASSISTANT_LANGUAGE, # assistant's language
            num=1, # number of results per page
            start=0, # index of the first result to retrieve
            stop=1, # the index of the last retrieved result
            pause=1.0): # delay between HTTP requests
            search_results.append(_)
            webbrowser.get().open(_)
    except:
        phrases = [
        'Seems like we have a trouble. See logs for more information']
        text = random.choice(phrases)
        play_voice_assistant_speech(core.ttsEngine, text)
        return
    print(search_results)
    phrases = [
        f'Here is what I found for {search_term} on google']
    text = random.choice(phrases)
    play_voice_assistant_speech(core.ttsEngine, text)


def search_for_video_on_youtube(*args: tuple) -> None:
    """YouTube search with automatic link opening
    """
    if not args[0]: return
    search_term = ' '.join(args[0])
    url = 'https://www.youtube.com/results?search_query=' + search_term
    webbrowser.get().open(url)
    phrases = [
        f'Here is what I found for {search_term} on youtube']
    text = random.choice(phrases)
    play_voice_assistant_speech(core.ttsEngine, text)
