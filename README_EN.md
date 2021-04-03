# Ahsoka Voice Assistant

## Installing PyAudio
The process for installing PyAudio will vary depending on your operating system.

**Debian Linux**

   If you’re on Debian-based Linux (like Ubuntu) you can install PyAudio with apt:
   `$ sudo apt-get install python-pyaudio python3-pyaudio`
   Once installed, you may still need to run pip install pyaudio, especially if you are working in a virtual environment.

**macOS**

For macOS, first you will need to install PortAudio with Homebrew, and then install PyAudio with pip:

`$ brew install portaudio`
`$ pip install pyaudio`

**Windows**

On Windows, you can install PyAudio with pip:

`$ pip install pyaudio`

## Testing the Installation
Once you’ve got PyAudio installed, you can test the installation from the console.

`$ python -m speech_recognition`

Make sure your default microphone is on and unmuted. If the installation worked, you should see something like this:

`A moment of silence, please...
Set minimum energy threshold to 600.4452854381937
Say something!`

Go ahead and play around with it a little bit by speaking into your microphone and seeing how well SpeechRecognition transcribes your speech.

## Supported File Types

Currently, SpeechRecognition supports the following file formats:

- WAV: must be in PCM/LPCM format
- AIFF
- AIFF-C
- FLAC: must be native FLAC format; OGG-FLAC is not supported
- If you are working on x-86 based Linux, macOS or Windows, you should be able to work with FLAC files without a problem. On other platforms, you will need to install a FLAC encoder and ensure you have access to the flac command line tool.

## Recognize methods

Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs.
These are:
- recognize_bing(): Microsoft Bing Speech
- recognize_google(): Google Web Speech API
- recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
- recognize_houndify(): Houndify by SoundHound
- recognize_ibm(): IBM Speech to Text
- recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
- recognize_wit(): Wit.ai

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. The other six all require an internet connection.
