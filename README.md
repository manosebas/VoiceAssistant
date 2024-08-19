# Voice Assistant

This Python script (`main.py`) functions as a conversational AI assistant. It integrates OpenAI's Whisper V3 for high-precision speech-to-text conversion, GPT-3.5 Turbo for generating contextually relevant responses, and OpenAI's Text-to-Speech (TTS) for delivering spoken replies.

## Key Features

- **Real-Time Speech Recognition**: Employs Whisper V3 to transform spoken words into text with high accuracy.
- **Smart Response Generation**: Utilizes GPT-3.5 Turbo to craft intelligent responses based on the user's input.
- **Speech Synthesis**: Converts generated text into speech using OpenAI's TTS, enabling smooth and natural interaction.
- **Hotword Activation**: Continuously listens for specific keywords to trigger interactions.

## Prerequisites

- Python 3.9+
- OpenAI's Whisper, GPT, and TTS models
- SpeechRecognition library
- PyTorch

## Installation

Make sure Python and the necessary dependencies are installed:

```
pip install openai speechrecognition torch
```

Set up your API key by visiting: https://platform.openai.com/api-keys
- Define API_KEY = "your_api_key"

Configure your assistant by visiting: https://platform.openai.com/assistants
- Set ASSISTANT_ID = "your_assistant_id"
- Set THREAD_ID = "your_thread_id"

## How to Use

- Microphone Setup: Ensure your microphone is correctly set up and selected as the default recording device.
- Run the Script: Launch the script with:
```
python main.py
```
- Interact: Start conversing with the assistant. Use hotwords like "Hey Manolo" to initiate commands. Loading the model may take some time.

## Command Line Options

- model: Define the Whisper model size (default: base). Options include tiny, base, small, medium, large.
- non_english: Select this option if using a non-English model.
- energy_threshold: Set the microphone's sensitivity to detect speech.
- record_timeout: Specify how real-time the recording should be, in seconds.
- phrase_timeout: Set the silence duration (in seconds) that indicates the end of a phrase.

## Configuration

- Customize the hot_words list in the script to define your preferred trigger words.
- Adjust the energy_threshold, record_timeout, and phrase_timeout settings to fine-tune speech detection based on your environment.

## Important Notes

- Verify that your API keys and model access permissions are correctly configured before running the script.
- The quality of the TTS output and the assistant's responsiveness will depend on the models selected and your system's performance.