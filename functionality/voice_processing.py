import sys  
sys.path = ['', '..'] + sys.path[1:]

import speech_recognition
from assistance_bot import core
from assistance_bot import settings


# listening and recognizing --------------------------------------------------
def listen_speech_from_mic(recognizer, microphone):
    """
    Adjust the recognizer sensitivity to ambient noise and record audio
    from the microphone
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    if not isinstance(microphone, speech_recognition.Microphone):
        raise TypeError('`microphone` must be `Microphone` instance')
    #listening
    try:
        with microphone as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print(f'Listening...')
            audio = recognizer.listen(
                mic, timeout = 10, phrase_time_limit = 10)
            return audio
    except speech_recognition.WaitTimeoutError:
        error = 'Error: Can you check if your microphone is on, please?'
        return error


def recognize_speech_from_mic(recognizer, audio) -> str:
    """
    Recognize audio recorded from the microphone
    """
    # check that recognizer argument are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    # recognize
    if type(audio) == str:
        return audio
    try:
        print(f'Started recognition...')
        data = recognizer.recognize_google(
            audio, language=core.assistant.language)
        recognized_data = str(data).lower()
        return recognized_data
    except speech_recognition.RequestError:
        error = 'Error: Check your Internet Connection, please'
        return error
    except speech_recognition.UnknownValueError:
        error = ''
        return error


# speaking -------------------------------------------------------------------
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
    else:
        print(text)
