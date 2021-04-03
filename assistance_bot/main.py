import sys  
sys.path = ['', '..'] + sys.path[1:]

import speech_recognition
from functionality.voice_recognition import recognition


if __name__ == '__main__':
    while True:
        # create recognizer and mic instances
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        # start speech recording with the subsequent output
        # of the recognized speech
        audio = recognition.listen_speech_from_mic(recognizer, microphone)
        text = recognition.recognize_speech_from_mic(recognizer, audio)
        print(text)
