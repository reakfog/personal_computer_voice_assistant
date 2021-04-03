import pyttsx3


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate',100)
engine.setProperty('voice', voices[-5].id)


def all_voices():
    for voice in voices:
        print ('Using voice:', repr(voice))
        engine.setProperty('voice',voice.id)
        engine.say(
            'Home Assistant is an open source home automation '
            'that puts local control and privacy first.')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()
