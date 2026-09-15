import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os

f = 44100
duration = 3
print("Status: Microphone is ON...")

while True:
   try:
      rd = sd.rec(int(duration * f), samplerate=f, channels=1)
      sd.wait()
      sf.write('t.wav', rd, f)
      r = sr.Recognizer()
      with sr.AudioFile('t.wav') as source:
         audio = r.record(source)
         tx = r.recognize_google(audio, language='ar-JO')
         print(f"You said: {tx}")
         os.system(f"say '{tx}'")
   except Exception as e:
      print(f"System Error: {e}")
   if os.path.exists('t.wav'): 
      try:
         os.remove('t.wav')
      except:
         pass