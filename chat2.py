import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os

def identify_dialect(text):
    db = {
        "Jordanian/Palestinian": ["يزم", "يا زلمة", "هسا", "شو في", "قرابة", "ليرة", "بديش"],
        "Egyptian": ["ده", "يا باشا", "إيه", "عايز", "كويس", "فين", "إزيك"],
        "Saudi": ["وشلونك", "إيش", "مرة", "تكفى", "أبشر", "زين"],
        "Syrian/Lebanese": ["شو", "بدي", "هيك", "هون", "تؤبرني", "منيح"],
        "Maghrebi": ["دابا", "بزاف", "واخا", "ديال", "شنو", "صافي"],
        "Iraqi": ["شكو", "ماكو", "خوش", "هواية", "يا به", "شلونك"]
    }
    
    words = text.split()
    for dialect, keywords in db.items():
        for word in words:
            if word in keywords:
                return dialect
    return "Unknown Dialect"

f = 44100
d = 4

print("Microphone is ON. Speak in any Arabic dialect...")

try:
    rd = sd.rec(int(d * f), samplerate=f, channels=1)
    sd.wait()
    print("Status: Microphone is OFF. Analyzing...")
    sf.write('temp.wav', rd, f)

    re = sr.Recognizer()
    with sr.AudioFile('temp.wav') as s:
        a = re.record(s)
        
        tx = re.recognize_google(a, language='ar-JO').lower()
        print(f"You said: {tx}")


        h = identify_dialect(tx)
        print(f"Result: {h}")
        

        os.system(f"say '{h}'")

except Exception as e:
    print(f"Error: {e}")