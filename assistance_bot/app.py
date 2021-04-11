import sys  
sys.path = ['', '..'] + sys.path[1:]

from assistance_bot import core
from functionality.voice_processing import *
from functionality.commands import *

if __name__ == '__main__':
    setup_assistant_voice(core.ttsEngine, core.assistant)
    while True:
        # start speech recording with the subsequent output
        # of the recognized speech
        audio = listen_speech_from_mic(core.recognizer, core.microphone)
        text = recognize_speech_from_mic(core.recognizer, audio)
        if text != '':
            print(text)
        # start speech synthesis
        execute_command(text)
