# Ahsoka Voice Assistant

## **Установка PyAudio**
Процесс установки PyAudio будет зависеть от вашей операционной системы.

**-----Debian Linux-----**

Если вы используете Linux на основе Debian (например, Ubuntu), вы можете установить PyAudio с помощью apt:

`sudo apt-get install python-pyaudio python3-pyaudio`

После установки вам все равно может потребоваться запуск pip install pyaudio, особенно если вы работаете в виртуальной среде.

**-----macOS------------**

Для macOS сначала необходимо установить PortAudio с Homebrew, а затем установить PyAudio с помощью pip:

`brew install portaudio`

**-----Windows----------**

В Windows вы можете установить PyAudio с помощью pip:

`pip install pyaudio`

## Тестирование установки
После того, как вы установили PyAudio, вы можете протестировать установку с консоли.

`python -m speech_recognition`

Убедитесь, что ваш микрофон по умолчанию включен и не заглушен. Если установка прошла успешно, вы должны увидеть что-то вроде этого:

`A moment of silence, please...
Set minimum energy threshold to 600.4452854381937
Say something!`

Попробуйте немного поиграть с этим, говоря в микрофон и посмотрев, насколько хорошо SpeechRecognition расшифровывает вашу речь.

## Поддерживаемые типы файлов
В настоящее время SpeechRecognition поддерживает следующие форматы файлов:

- WAV: должен быть в формате PCM / LPCM
- AIFF
- AIFF-C
- FLAC: должен быть в собственном формате FLAC; OGG-FLAC не поддерживается

Если вы работаете с Linux, macOS или Windows на базе x-86, вы сможете без проблем работать с файлами FLAC. На других платформах вам потребуется установить кодировщик FLAC и убедиться, что у вас есть доступ к flac инструменту командной строки.

## Recognize методы

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
