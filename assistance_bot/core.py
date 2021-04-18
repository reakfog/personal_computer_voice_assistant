import speech_recognition
import pyttsx3
from . import settings


class VoiceAssistant:
    """Voice assistant settings including name, gender, language of speech
    """
    name = settings.ASSISTANT_NAME
    sex = settings.SEX
    language = settings.ASSISTANT_LANGUAGE


class AssistantOwner:
    """Owner information, including name, city of residence,
    native language of speech, target language (for text translations)
    """
    name = settings.OWNER_NAME
    home_city = settings.HOME_CITY
    native_language = settings.NATIVE_LANGUAGE
    target_language = settings.TARGET_LANGUAGE


# create recognizer and mic instances
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
# create text_to_speech engine and assistant instances
ttsEngine = pyttsx3.init()
assistant = VoiceAssistant()
owner = AssistantOwner()
