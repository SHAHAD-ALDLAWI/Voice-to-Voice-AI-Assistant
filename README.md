# 🎤 Voice-to-Voice AI Assistant

An intelligent assistant that converts natural speech into AI understanding and an audio response.

---

## 📋 The Three Basic Steps
* **Step 1 (Speech-to-Text):** 🎤 User's voice → Converted to text (Google STT)
* **Step 2 (LLM Processing):** 🤖 Processed using LLM (Cohere API)
* **Step 3 (Text-to-Speech):** 🔊 Converted back to audio and played to the user

---

## 📸 Demo & Execution Result
Here is how the project looks and runs in action:

> **Terminal Output Screenshot:**  
> ![Terminal Output](terminal_output.png)

**Terminal Text Output Example:**
```text

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
```

---

## 🔧 Requirements and Installation

### 1️⃣ Install Required Libraries
Run the following command to install dependencies:
```bash
pip install --break-system-packages SpeechRecognition
pip install --break-system-packages pyttsx3
pip install --break-system-packages cohere
```
Or use requirements.txt:
```bash
pip install -r requirements.txt --break-system-packages
```

### 2️⃣ Get a Cohere API Key
* Go to cohere.ai
* Create a free account
* Copy the API Key from your control panel

### 3️⃣ Set Environment Variable
* **Linux/Mac:**
  ```bash
  export COHERE_API_KEY="your-api-key-here"
  ```
* **Windows (PowerShell):**
  ```powershell
  $env:COHERE_API_KEY="your-api-key-here"
  ```

---

## 🚀 How to Run
Execute the main script using Python:
```bash
python main.py
```

**Execution Options:**
* **Single Cycle:** Record a single voice input and get a single response.
* **Continuous Run:** A repeating loop waiting for your commands (`Ctrl+C` to exit).

---

## 📊 Code Explanation

### 1. Speech Recognition (STT)
```python
import speech_recognition as sr

recognizer = sr.Recognizer()
with microphone as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language="ar-SA")
```
* Receives audio from the microphone.
* Converts it into written text.
* Supports Arabic language 🇸🇦.

### 2. LLM Processing
```python
import cohere

response = cohere_client.chat(
    model="command-r-08-2024",
    messages=[{"role": "user", "content": user_text}]
)
ai_response = response.message.content[0].text
```
* Sends text to the Cohere model.
* Performs natural language processing.
* Retrieves an intelligent response.

### 3. Text-to-Speech (TTS)
```python
import pyttsx3

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
```
* Converts text into speech.
* Plays audio directly to the user.

---

## ⚙️ Customizable Variables
You can modify these settings directly in the code:
```python
# Speech rate (0-100+)
self.tts_engine.setProperty('rate', 150)

# Volume level (0.0-1.0)
self.tts_engine.setProperty('volume', 1.0)

# Cohere Model
model="command-r-08-2024"

# Language
language="ar-SA"  # Arabic or "en-US" for English
```

---

## 🐛 Troubleshooting

* **Issue: "Could not understand speech"**
  * *Solution:* Make sure the microphone is clear, speak closer to it, and reduce ambient noise.
* **Issue: "Connection error"**
  * *Solution:* Check your internet connection or use a VPN if required.
* **Issue: Audio not working**
  * *Solution:* Check speaker settings or test with: 
    ```bash
    python -c "import pyttsx3; pyttsx3.init().say('test'); pyttsx3.init().runAndWait()"
    ```

---

## 📁 Project Structure
```text
voice-assistant/
├── main.py                # Main script file
├── requirements.txt       # Required Python libraries
├── README.md              # Documentation file
├── terminal_output.png    # Execution screenshot
└── response.mp3           # Generated audio file (optional)
```

---

## 🎯 Next Steps & Future Enhancements
* **Save Audio:** Save responses directly to a file:
  ```python
  engine.save_to_file(text, 'response.mp3')
  ```
* **Multi-language Support:** Easily switch between Arabic and English.
* **Context Memory:** Add chat history to maintain conversation context.
* **Graphical Interface (GUI):** Build a dashboard using Flask or Streamlit.

---

## 📚 Useful Resources and Links
* [Cohere API Docs](https://docs.cohere.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pyttsx3 Docs](https://pypi.org/project/pyttsx3/)

---

## 📝 Important Notes
* ✅ The code fully supports the Arabic language.
* ✅ Libraries are free to use (Cohere includes a Free Tier).
* ⚠️ Requires an internet connection because Google STT and Cohere API run on the cloud.
* ⚠️ Keep your API Key secure and do not push it publicly to GitHub.
