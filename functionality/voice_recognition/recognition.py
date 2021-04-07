import speech_recognition
from .utils import current_datetime


def listen_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    if not isinstance(microphone, speech_recognition.Microphone):
        raise TypeError('`microphone` must be `Microphone` instance')
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    try:
        with microphone as mic:
            recognizer.adjust_for_ambient_noise(mic,  duration=1)
            print(f'Listening...{current_datetime()}')
            audio = recognizer.listen(mic, timeout = 10, phrase_time_limit = 10)
            print(f'Ok, I see...{current_datetime()}')
            return audio
    except speech_recognition.WaitTimeoutError:
        mic_error = 'Can you check if your microphone is on, please?'
        return mic_error


def recognize_speech_from_mic(recognizer, speech):
    # check that recognizer argument are appropriate type
    if not isinstance(recognizer, speech_recognition.Recognizer):
        raise TypeError('`recognizer` must be `Recognizer` instance')
    # recognize audio recorded from the microphone
    if type(speech) == str:
        return speech
    try:
        print(f'Started recognition...{current_datetime()}')
        data = recognizer.recognize_google(speech, language='ru')
        print(f'Finish recognition...{current_datetime()}')
        recognized_data = str(data).lower()
        return recognized_data
    except speech_recognition.UnknownValueError as error:
        recognition_error = str(error)
        return recognition_error
    except speech_recognition.RequestError:
        recognition_error = 'Check your Internet Connection, please'
        return recognition_error
    except Exception:
        return speech
