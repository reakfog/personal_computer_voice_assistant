import sys  
sys.path = ['', '..'] + sys.path[1:]

import speech_recognition
import pyttsx3
from functionality.voice_recognition import recognition
from functionality.voice_synthesis import voice


if __name__ == '__main__':
    # create recognizer and mic instances
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    # create text_to_speech engine and assistant instances
    ttsEngine = pyttsx3.init()
    assistant = voice.VoiceAssistant()
    voice.setup_assistant_voice(ttsEngine, assistant)
    while True:
        # start speech recording with the subsequent output
        # of the recognized speech
        audio = recognition.listen_speech_from_mic(recognizer, microphone)
        text = recognition.recognize_speech_from_mic(recognizer, audio)
        print(text)
        # start speech synthesis
        voice.play_voice_assistant_speech(ttsEngine, text)
