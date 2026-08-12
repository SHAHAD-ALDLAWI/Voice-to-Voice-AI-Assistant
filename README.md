🎤 Voice-to-Voice AI Assistant

A simple Voice-to-Voice AI Assistant built with Python.

The project converts the user's speech into text, sends the text to an LLM for processing, and then converts the AI response back into speech.

🔗 Main Technologies
Python
SpeechRecognition
 — Speech-to-Text
Cohere API
 — LLM Processing
pyttsx3
 — Text-to-Speech
📋 How It Works

The assistant works through three basic steps:

1️⃣ Speech-to-Text (STT)

User's Voice → Text

The microphone captures the user's voice and SpeechRecognition
 uses Google's Speech Recognition service to convert it into text.

Arabic is supported using the ar-SA language code.

2️⃣ LLM Processing

Text → AI Response

The transcribed text is sent to the Cohere Chat API
, which processes the user's request and generates an intelligent response.

The project currently uses:

command-r-08-2024


More information about this model is available in the Cohere Command R documentation
.

3️⃣ Text-to-Speech (TTS)

AI Response → Audio

The generated response is converted into speech using pyttsx3
 and played through the computer's speakers.

📸 Demo & Execution Result

The project runs directly from the terminal.

Terminal Output 

> ![Terminal Output](terminal_output.png)

Example

    ║   🎤 مساعد صوتي ذكي 🎤              ║

    
أدخل Cohere API Key: 

✅ تم تهيئة المساعد الصوتي

 اختر الوضع:
1️⃣  دورة واحدة فقط
2️⃣  تشغيل مستمر

اختيارك (1 أو 2): 1

🎤 جاهز للاستماع... (تحدث الآن)
📝 النص المحول: انا اسمي شهد

🤖 معالجة النص...
💬 رد المساعد: مرحبًا شهد، يسعدني مساعدتك! كيف يمكنني أن أكون مفيدًا لك اليوم؟

🔊 تحويل النص إلى صوت...
✅ تم تشغيل الصوت

⚙️ Requirements

Before running the project, make sure you have:

Python 3 installed
A working microphone
Speakers or headphones
An active internet connection
A Cohere API Key
🔗 Required Libraries
SpeechRecognition
pyttsx3
Cohere Python SDK

Note: SpeechRecognition's microphone functionality requires an audio backend such as PyAudio. See the SpeechRecognition documentation
 for installation details.

🔧 Installation
1️⃣ Install Required Libraries

Install the dependencies using:

pip install --break-system-packages SpeechRecognition
pip install --break-system-packages pyttsx3
pip install --break-system-packages cohere


Or, if you have a requirements.txt file:

pip install -r requirements.txt --break-system-packages

🔗 Package Documentation
SpeechRecognition
pyttsx3
Cohere Python SDK
🔑 Get a Cohere API Key

The project requires a Cohere API key to communicate with the LLM.

Steps
Create an account on Cohere
.
Open the Cohere Dashboard
.
Create or copy your API key.
Store the key securely.
Do not upload the API key to GitHub.
🔗 Useful Cohere Links
Cohere Website
Cohere Dashboard
Cohere Documentation
Cohere Chat API
🌍 Set the API Key

Instead of writing the API key directly inside the Python code, use an environment variable.

Linux / macOS
export COHERE_API_KEY="your-api-key-here"

Windows PowerShell
$env:COHERE_API_KEY="your-api-key-here"


⚠️ Never commit your API key to GitHub.

It is recommended to add sensitive files such as .env to .gitignore if you use them in your project.

🚀 How to Run

Run the main Python script:

python main.py


The program will ask you to choose between two modes.

1️⃣ Single Cycle

Records one voice input, processes it using the AI, and plays one response.

1

2️⃣ Continuous Run

Keeps listening for new commands and responding continuously.

2


Press:

Ctrl + C


to stop the continuous mode.

🧠 Code Explanation
🎤 Speech Recognition
import speech_recognition as sr

recognizer = sr.Recognizer()

with microphone as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(
        audio,
        language="ar-SA"
    )


This section:

Captures audio from the microphone.
Converts the user's speech into text.
Uses Arabic (ar-SA) for speech recognition.
🔗 Documentation

SpeechRecognition Library Reference

🤖 LLM Processing
import cohere

response = cohere_client.chat(
    model="command-r-08-2024",
    messages=[
        {
            "role": "user",
            "content": user_text
        }
    ]
)

ai_response = response.message.content[0].text


This section:

Sends the transcribed text to Cohere.
Processes the request using the selected model.
Retrieves the generated AI response.
🔗 Documentation
Cohere Chat API
Cohere API Reference
Command R Documentation
🔊 Text-to-Speech
import pyttsx3

engine = pyttsx3.init()

engine.say(text)
engine.runAndWait()


This section converts the AI response into speech and plays it through the default audio output.

🔗 Documentation

pyttsx3 Documentation

⚙️ Customizable Variables

You can modify several settings directly in the code.

🔊 Speech Rate
self.tts_engine.setProperty('rate', 150)


Controls how quickly the assistant speaks.

🔊 Volume
self.tts_engine.setProperty('volume', 1.0)


Controls the audio volume.

The value ranges from:

0.0 → 1.0

🤖 Cohere Model
model="command-r-08-2024"

🌍 Speech Recognition Language

Arabic:

language="ar-SA"


English:

language="en-US"

🐛 Troubleshooting
❌ Could not understand speech

Possible solutions:

Make sure the microphone is working.
Speak closer to the microphone.
Reduce background noise.
Try speaking more clearly.
Check that the correct microphone is selected.
🔗 SpeechRecognition Documentation

SpeechRecognition Library

❌ Connection Error

The project depends on online services for speech recognition and AI processing.

Possible solutions:

Check your internet connection.
Make sure your Cohere API key is valid.
Check the Cohere API status/documentation
.
🔊 Audio Not Working

Make sure your speakers or headphones are connected and configured correctly.

You can test pyttsx3 using:

python -c "import pyttsx3; engine=pyttsx3.init(); engine.say('test'); engine.runAndWait()"

🔗 pyttsx3 Documentation

pyttsx3 on PyPI

📁 Project Structure
voice-assistant/
│
├── main.py                 # Main Python script
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── terminal_output.png     # Terminal execution screenshot
└── response.mp3            # Generated audio file (optional)

🎯 Future Enhancements

The project can be extended with additional features in the future.

💾 Save Audio

Save the generated response as an audio file:

engine.save_to_file(text, 'response.mp3')

🌍 Multi-language Support

Add support for additional languages, such as:

Arabic 🇸🇦
English 🇺🇸
Other supported languages
🧠 Context Memory

Add conversation history so the assistant can remember previous messages.

🖥️ Graphical User Interface

Build a graphical interface using tools such as:

Flask
Streamlit
📚 Useful Resources
🤖 Cohere
Cohere Website
Cohere Documentation
Cohere Chat API
Cohere Python SDK
🎤 SpeechRecognition
GitHub Repository
Library Reference
🔊 pyttsx3
PyPI
GitHub Repository
📝 Important Notes
✅ The project supports Arabic speech recognition using ar-SA.
✅ The project can be used with English by changing the language to en-US.
🌐 An internet connection is required for Google Speech Recognition and Cohere API requests.
🔐 Keep your Cohere API key private.
⚠️ Never upload API keys or other secrets to GitHub.
