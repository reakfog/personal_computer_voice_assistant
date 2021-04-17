import sys  
sys.path = ['', '..'] + sys.path[1:]

import daemon
from assistance_bot import core
from functionality.voice_processing import speaking, listening
from functionality.commands import *

if __name__ == '__main__':
    speaking.setup_assistant_voice(core.ttsEngine, core.assistant)
    while True:
        # start speech recording and speech recognition
        recognized_speech = listening.get_listen_and_recognize_result(
            core.recognizer,
            core.microphone)
        # executing the given command
        execute_command(recognized_speech)
