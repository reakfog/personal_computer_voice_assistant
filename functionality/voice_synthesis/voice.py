import sys  
sys.path = ['', '..'] + sys.path[1:]

from assistance_bot import settings


class VoiceAssistant:
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = settings.ASSISTANT_NAME
    sex = settings.SEX
    speech_language = settings.SPEECH_LANGUAGE
    recognition_language = settings.RECOGNITION_LANGUAGE

def setup_assistant_voice(engine, assistant_obj):
    """
    Установка голоса по умолчанию (индекс может меняться в 
    зависимости от настроек операционной системы)
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

def play_voice_assistant_speech(engine, speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    engine.say(speech)
    engine.runAndWait()
