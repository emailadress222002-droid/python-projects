import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import re

f = 44100
duration = 5
user = input("enter: ")
try:
   print("\n🎤 Listening...")
   rd = sd.rec(int(f * duration), samplerate=f, channels=1)
   sd.wait()
   sf.write('t.wav', rd, f)
   r = sr.Recognizer()
   with sr.AudioFile('t.wav') as s:
      a = r.record(s)
      text = r.recognize_google(a, language="en-UK").lower()
      if text in user:
         print("right ")
         os.system("say 'right'")
      else:
         print("wrong")
         os.system("say 'wrong'")
except:
   pass