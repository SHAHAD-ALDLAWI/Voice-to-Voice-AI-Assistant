import os
import sys
import json
from pathlib import Path
 
# Speech-to-Text
try:
    import speech_recognition as sr
except ImportError:
    print("Installing speech_recognition...")
    os.system("pip install --break-system-packages SpeechRecognition")
    import speech_recognition as sr
 
# Text-to-Speech
try:
    import pyttsx3
except ImportError:
    print("Installing pyttsx3...")
    os.system("pip install --break-system-packages pyttsx3")
    import pyttsx3
 
# LLM (Cohere)
try:
    import cohere
except ImportError:
    print("Installing cohere...")
    os.system("pip install --break-system-packages cohere")
    import cohere
 
class VoiceAssistant:
    def __init__(self, api_key=None):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 1.0)
        
        api_key = api_key or os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("⚠️  يجب تعيين COHERE_API_KEY")
        
        self.cohere_client = cohere.ClientV2(api_key=api_key)
        print("✅ تم تهيئة المساعد الصوتي")
    
    def step1_speech_to_text(self):
        print("\n🎤 جاهز للاستماع... (تحدث الآن)")
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10)
            
            text = self.recognizer.recognize_google(audio, language="ar-SA")
            print(f"📝 النص المحول: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ لم أتمكن من فهم الكلام، حاول مرة أخرى")
            return None
        except sr.RequestError:
            print("❌ خطأ في الاتصال بخدمة التعرف على الصوت")
            return None
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    def step2_process_with_llm(self, user_text):
        print(f"\n🤖 معالجة النص...")
        try:
            response = self.cohere_client.chat(
                model="command-r-08-2024",
                messages=[{"role": "user", "content": user_text}]
            )
            ai_response = response.message.content[0].text
            print(f"💬 رد المساعد: {ai_response}")
            return ai_response
        except Exception as e:
            print(f"❌ خطأ في معالجة النص: {e}")
            return "عذراً، حدث خطأ في المعالجة"
    
    def step3_text_to_speech(self, text):
        print(f"\n🔊 تحويل النص إلى صوت...")
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            print(f"✅ تم تشغيل الصوت")
        except Exception as e:
            print(f"❌ خطأ في تحويل النص إلى صوت: {e}")
    
    def run_cycle(self):
        user_text = self.step1_speech_to_text()
        if not user_text:
            return
        ai_response = self.step2_process_with_llm(user_text)
        if not ai_response:
            return
        self.step3_text_to_speech(ai_response)
    
    def run_continuous(self, max_cycles=None):
        cycles = 0
        try:
            while True:
                print("\n" + "="*50)
                print(f"دورة #{cycles + 1}")
                print("="*50)
                self.run_cycle()
                cycles += 1
                if max_cycles and cycles >= max_cycles:
                    break
                input("\n👉 اضغط Enter للمتابعة (أو Ctrl+C للخروج)...")
        except KeyboardInterrupt:
            print("\n\n👋 وداعاً!")

def main():
    print("""
    ╔═══════════════════════════════════════╗
    ║   🎤 مساعد صوتي ذكي 🎤              ║
    ╚═══════════════════════════════════════╝
    """)
    
    if not os.getenv("COHERE_API_KEY"):
        api_key = input("أدخل Cohere API Key: ").strip()
        os.environ["COHERE_API_KEY"] = api_key
    
    try:
        assistant = VoiceAssistant()
        print("\n اختر الوضع:")
        print("1️⃣  دورة واحدة فقط")
        print("2️⃣  تشغيل مستمر")
        choice = input("\nاختيارك (1 أو 2): ").strip()
        
        if choice == "1":
            assistant.run_cycle()
        else:
            assistant.run_continuous()
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()