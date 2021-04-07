# Ahsoka Voice Assistant

## Содержание
1. [Описание проекта](#description)
2. [Стэк технологий](#stack)
3. [Технические требования](#requirements)
4. [Установка PyAudio и других пакетов](#pacages_installation)
- 4.1. [Debian Linux](#pyaudio_installation_linux)
- 4.2. [Windows](#pyaudio_installation_macos)
- 4.3. [Windows](#pyaudio_installation_windows)
- 4.4. [Установка python зависимостей](#python_packages_installation)
5. [Запуск проекта локально](#lounch)
6. [Тестирование SpeechRecognition](#sr_testing)
7. [Поддерживаемые типы audio-файлов](#supported_audio_file_types)
8. [Recognize методы](#recognize_methods)
9. [Полезные ссылки](#links)

## <a name='description'>Описание проекта</a>

## <a name='stack'>Стек технологий</a>
Python3, PyAudio

## <a name='requirements'>Технические требования</a>
Все необходимые пакеты перечислены в [requirements.txt](https://github.com/reakfog/ahsoka_voice_assistant/blob/main/requirements.txt)

## <a name='pacages_installation'>Установка PyAudio и других пакетов</a>
Процесс установки PyAudio будет зависеть от вашей операционной системы.

#### <a name='pyaudio_installation_linux'>Debian Linux</a>
Если вы используете Linux на основе Debian (например, Ubuntu), вы можете установить PyAudio с помощью apt:

`sudo apt-get install python3-pyaudio portaudio19-dev python-all-dev python3-all-dev flac libespeak-dev`
or
`sudo apt-get install python-pyaudio portaudio19-dev python-all-dev python3-all-dev flac libespeak-dev`

После установки вам все равно может потребоваться запуск pip install pyaudio, особенно если вы работаете в виртуальной среде.

#### <a name='pyaudio_installation_macos'>macOS</a>
Для macOS сначала необходимо установить PortAudio с Homebrew, а затем установить PyAudio с помощью pip:

`brew install portaudio`

#### <a name='pyaudio_installation_windows'>Windows</a>
В Windows вы можете установить PyAudio с помощью pip:

`pip install pyaudio`

#### <a name='python_packages_installation'>Установка python зависимостей</a>
Установите необходимые библиотеки:

`pip install -r requirements.txt`

## <a name='lounch'>Запуск проекта локально</a>

## <a name='sr_testing'>Тестирование установки speech_recognition</a>
После того, как вы установили PyAudio, вы можете протестировать установку с консоли.

`python -m speech_recognition`

Убедитесь, что ваш микрофон по умолчанию включен и не заглушен. Если установка прошла успешно, вы должны увидеть что-то вроде этого:

`A moment of silence, please...
Set minimum energy threshold to 600.4452854381937
Say something!`

Попробуйте немного поиграть с этим, говоря в микрофон и посмотрев, насколько хорошо SpeechRecognition расшифровывает вашу речь.

## <a name='supported_audio_file_types'>Поддерживаемые типы audio-файлов</a>
В настоящее время SpeechRecognition поддерживает следующие форматы файлов:

- WAV: должен быть в формате PCM / LPCM
- AIFF
- AIFF-C
- FLAC: должен быть в собственном формате FLAC; OGG-FLAC не поддерживается

Если вы работаете с Linux, macOS или Windows на базе x-86, вы сможете без проблем работать с файлами FLAC. На других платформах вам потребуется установить кодировщик FLAC и убедиться, что у вас есть доступ к flac инструменту командной строки.

## <a name='recognize_methods'>Recognize методы</a>

Каждый Recognizer экземпляр имеет семь методов распознавания речи из источника звука с использованием различных API.
Это:
- recognize_bing(): Microsoft Bing Speech
- recognize_google(): API Google Web Speech
- recognize_google_cloud(): Google Cloud Speech - требуется установка пакета google-cloud-speech.
- recognize_houndify(): Houndify от SoundHound
- recognize_ibm(): IBM Speech to Text
- recognize_sphinx(): CMU Sphinx - требуется установка PocketSphinx
- recognize_wit(): Wit.ai

Из семи методов только recognize_sphinx()работает в автономном режиме с движком CMU Sphinx. Остальные шесть требуют подключения к Интернету.

## <a name='links'>Полезные ссылки</a>
- [Python speech recognition](https://realpython.com/python-speech-recognition/)
- [SpeechRecognition documentation](https://github.com/Uberi/speech_recognition)
