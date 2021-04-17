import sys

import assistance_bot  
sys.path = ['', '..'] + sys.path[1:]

import speech_recognition
from termcolor import colored
from assistance_bot import core


def listen_speech_from_mic(recognizer, microphone) -> speech_recognition.AudioData:
    """
    Adjust the recognizer sensitivity to ambient noise and record audio
    from the microphone
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    if not isinstance(microphone, speech_recognition.Microphone):
        raise TypeError('`microphone` must be `Microphone` instance')
    recognizer.energy_threshold = 300
    with microphone as mic:
        recognizer.adjust_for_ambient_noise(
            mic,
            duration=1)
        print(f'Listening...')
        audio = recognizer.listen(
            mic,
            timeout = None,
            phrase_time_limit = 10,
            snowboy_configuration=None)
        return audio


def recognize_speech_from_audio(recognizer, audio) -> str:
    """
    Recognize audio recorded from the microphone
    """
    # check that recognizer argument are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    # recognize
    print(f'Started recognition...')
    data = recognizer.recognize_google(
        audio_data=audio,
        key=None,
        language=core.assistant.language,
        show_all=False)
    recognized_data = str(data).lower()
    return recognized_data


def get_listen_and_recognize_result(recognizer, microphone) -> str:
    assistant = core.assistant.name
    owner = core.owner.name
    error_indicator = 'Error:'
    try:
        audio = listen_speech_from_mic(recognizer, microphone)
    except speech_recognition.WaitTimeoutError:
        error = 'Can you check if your microphone is on, please?'
        text = ''.join([assistant, ': ', colored(error, 'yellow')])
        print(text)
        return ''.join([error_indicator, error])
    try:
        speech = recognize_speech_from_audio(recognizer, audio=audio)
        text = ''.join([owner, ': ', colored(speech.capitalize(), 'green')])
        print(text)
        return speech
    except speech_recognition.RequestError:
        error = 'I could not request results from service'
        text = ''.join([assistant, ': ', colored(error, 'red')])
        print(text)
        return ''.join([error_indicator, error])
    except speech_recognition.UnknownValueError:
        return ''
