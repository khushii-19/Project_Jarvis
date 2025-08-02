# Project_Jarvis

# Jarvis - Voice-Activated Virtual Assistant 🔊🤖

**Jarvis** is a voice-activated virtual assistant built in Python. It performs tasks like browsing the web, playing music, fetching news, and answering general queries using Google's **Gemini Pro (via Generative AI API)**. Designed to behave like Alexa or Google Assistant, Jarvis responds to your voice after hearing the wake word "Jarvis."

---

## 🧠 Short Description

Jarvis is a lightweight AI-powered desktop assistant that listens for commands, responds via speech, and uses Gemini for intelligent replies. It combines voice recognition, text-to-speech, browsing, music, and real-time news capabilities in a single Python script.

---

## ✨ Features

- 🔊 **Voice Recognition**
  - Uses `speech_recognition` to detect voice input.
  - Activates on hearing **"Jarvis"**.

- 🗣️ **Text-to-Speech**
  - Local TTS via `pyttsx3`.
  - Optional online voice using `gTTS` and `pygame`.

- 🌐 **Web Browsing**
  - Opens popular websites like Google, YouTube, LinkedIn, etc.

- 🎵 **Music Playback**
  - Connects to a `musicLibrary` module to stream songs via web links.

- 📰 **News Fetching**
  - Integrates with **NewsAPI** to read current headlines aloud.

- 🧠 **Gemini AI Integration**
  - Uses Google's `gemini-2.5-pro` model for intelligent responses to open-ended questions.

---

## 🔄 Workflow

1. **Initialization**
   - Prints and speaks "Initializing Jarvis..."

2. **Wake Word Detection**
   - Continuously listens for the wake word **"Jarvis"**.

3. **Activation**
   - Replies with "Ya" once activated.

4. **Command Recognition**
   - Listens for commands and performs actions like:
     - Opening websites
     - Playing music
     - Fetching news
     - Talking via Gemini AI

5. **Speech Output**
   - Responds using either local or online text-to-speech.

---

## 🧩 Libraries Used

- `speech_recognition` – Voice command input  
- `pyttsx3` – Local TTS engine  
- `gTTS` + `pygame` – Google voice + audio playback  
- `webbrowser` – For opening URLs  
- `requests` – For API calls  
- `google.generativeai` – Gemini API for smart replies  
- `os`, `dotenv` – Environment config  
- `musicLibrary` – Custom module for music links  
- `NewsAPI` – For news headlines  

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/jarvis-voice-assistant.git
   cd jarvis-voice-assistant

   Install dependencies
pip install -r requirements.txt

Set up your .env file
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key

Run the project
python main.py

Important Notes
Never push your .env file to GitHub. Add it to .gitignore.

Ensure your microphone is connected and working.

The musicLibrary module should return a valid YouTube/music link based on the song name.

Acknowledgements
Google Gemini for AI responses

NewsAPI for real-time headlines

Open-source TTS and voice recognition libraries

Built with 💡 by Khushi Gupta
