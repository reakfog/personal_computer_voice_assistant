# Personal computer Voice Assistant

## Содержание
1. [Описание проекта](#description)
2. [Стэк технологий](#stack)
3. [Технические требования](#requirements)
4. [Установка зависимостей и запуск проекта локально](#pacages_installation_and_lounch)
    - [Debian Linux](#pyaudio_installation_linux)
    - [macOS](#pyaudio_installation_macos)
    - [Windows](#pyaudio_installation_windows)
5. [Тестирование SpeechRecognition](#sr_testing)
6. [Полезные ссылки](#links)

## <a name='description'>Описание проекта</a>
Персональный голосовой ассистент. Масштабируемое приложение, где каждый может не разбираясь в коде проекта дописать в и без того большой список функций нужный ему функционал. Есть лист пользовательских настроек. Проект находится на стадии разработки, но уже готов к использованию.

Данный проект голосового ассистента на Python 3 для Windows и Linux и macOS умеет:

- воспроизводить случайное приветствие
- воспроизводить случайное прощание с последующим завершением работы программы

В разработке:

- сообщать о прогнозе погоды в указанной точке мира
- производить поисковый запрос в поисковой системе Google
- производить поисковый запрос видео на сайте YouTube
- выполнять поиск определения в Wikipedia
- и многое другое
## <a name='stack'>Стек технологий</a>
Python3, python3-pyaudio, portaudio19-dev, python-all-dev, python3-all-dev, flac, libespeak-dev

## <a name='requirements'>Технические требования</a>
Все необходимые пакеты перечислены в [requirements.txt](https://github.com/reakfog/ahsoka_voice_assistant/blob/main/requirements.txt)

## <a name='lounch'>Установка зависимостей и запуск проекта локально</a>
- `python -m venv venv` - создание виртуального окружения
- `source venv/bin/activate` - автивация витуального окружения
Процесс установки пакетов будет зависеть от вашей операционной системы.
- *<a name='pyaudio_installation_linux'>Debian Linux</a>*
    - `sudo apt-get install python3-pyaudio portaudio19-dev python-all-dev python3-all-dev flac libespeak-dev`
    or
    - `sudo apt-get install python-pyaudio portaudio19-dev python-all-dev python3-all-dev flac libespeak-dev`
- *<a name='pyaudio_installation_macos'>macOS</a>*
    - `brew install portaudio`
- *<a name='pyaudio_installation_windows'>Windows</a>*
    - Если Вы используете Windows не требуется дополнительных действий
- `pip install -r requirements.txt` - установка python зависимостей
- `python assistance_bot/app.py` - запуск проекта

## <a name='sr_testing'>Тестирование установки speech_recognition</a>
После того, как вы установили PyAudio, вы можете протестировать установку с консоли.

`python -m speech_recognition`

Убедитесь, что ваш микрофон по умолчанию включен и не заглушен. Если установка прошла успешно, вы должны увидеть что-то вроде этого:

> A moment of silence, please...
> Set minimum energy threshold to 600.4452854381937
> Say something!

Попробуйте немного поиграть с этим, говоря в микрофон и посмотрев, насколько хорошо SpeechRecognition расшифровывает вашу речь.

## <a name='links'>Полезные ссылки</a>
- [Python speech recognition](https://realpython.com/python-speech-recognition/)
- [SpeechRecognition documentation](https://github.com/Uberi/speech_recognition)
