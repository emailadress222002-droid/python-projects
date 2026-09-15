import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import re
import webbrowser

f = 44100
d = 3
print("Status: Microphone is ON. Speak (e.g., 1000 divide 80)")

try:
    rd = sd.rec(int(d * f), samplerate=f, channels=1)
    sd.wait()
    sf.write('t.wav', rd, f)

    r = sr.Recognizer()
    with sr.AudioFile('t.wav') as source:
        audio = r.record(source)
        
        tx = r.recognize_google(audio, language='en-us').lower()
        print(f"You said: {tx}")
        if "t" in tx:
            webbrowser.open("https://bommm.oneapp.dev")
except Exception as e:
    print(f"System Error: {e}")