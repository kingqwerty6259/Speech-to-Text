# Speech Recognition Script

## Overview

This script utilizes the `speech_recognition` library to listen to your microphone input and transcribe it into text using Google's speech recognition API. The program continuously listens for speech, converts it into text, and prints the transcribed text to the console.

## Requirements

- Python 3.x
- `speech_recognition` library
- Microphone and sound input device (e.g., built-in mic or external microphone)

### Installation

You can install the required library by running:
```bash
pip install SpeechRecognition
```

Additionally, ensure that you have the required dependencies for your platform to capture microphone input. On Linux, for example, you may need to install `pyaudio`:
```bash
pip install pyaudio
```

## How to Use

1. Run the script.
2. The script will continuously listen to your microphone.
3. Once you speak, it will print your speech in lowercase text.
4. If an error occurs (such as microphone disconnection), it will print `...` and reset the recognizer to continue listening.

## Code Explanation

- **Recognizer Initialization**:  
  The script initializes a `Recognizer` object (`r = sr.Recognizer()`), which is used to process audio.
  
- **Continuous Loop**:  
  The script uses a `while True` loop, meaning it will continuously run, listening for input.
  
- **Microphone Input**:  
  The `with sr.Microphone() as source` statement listens to the microphone and stores the audio into the `audio` variable.
  
- **Speech to Text**:  
  The `r.recognize_google(audio)` function sends the audio data to Google’s speech recognition API and returns the text version of the speech. The text is converted to lowercase before printing it.

- **Error Handling**:  
  If an error occurs (e.g., no speech detected or microphone issue), the program will print `...`, reset the recognizer, and continue listening.

## Example

```plaintext
Connected
hello world
Connected
how are you today
Connected
...
```

The script continuously listens, transcribes speech, and prints the output in real-time.
