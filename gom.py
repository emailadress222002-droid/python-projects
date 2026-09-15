import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import re
import webbrowser
import cv2
import shutil

f = 44100
duration = 2.5 
print("Status: Assistant is ON. Speak math or commands...")

try:
    while True:
        print("\n🎤 Listening...")
        rd = sd.rec(int(duration * f), samplerate=f, channels=1)
        sd.wait()
        sf.write('t.wav', rd, f)

        r = sr.Recognizer()
        with sr.AudioFile('t.wav') as source:
            audio = r.record(source)
            
            try:
                tx = r.recognize_google(audio, language='ar-JO').lower()
                txn = r.recognize_google(audio, language='en-US').lower()
                print(f"Ar: {tx} | En: {txn}")
            except:
                continue
            nums = [int(s) for s in re.findall(r'\d+', tx)]
            if len(nums) >= 2:
                res = None
                if any(x in tx for x in ['على', 'تقسيم', 'تقسم', '/', '÷']):
                    res = nums[0] / nums[1]
                elif any(x in tx for x in ['ضرب', 'في', 'بـ', 'x', '*']):
                    res = nums[0] * nums[1]
                elif any(x in tx for x in ['ناقص', '-']):
                    res = nums[0] - nums[1]
                elif any(x in tx for x in ['زائد', '+', 'و']):
                    res = nums[0] + nums[1]
                
                if res is not None:
                    final = int(res) if res == int(res) else round(res, 2)
                    print(f"Result: {final}")
                    os.system(f"say {final}")
                    continue
            if "مصنع" in tx or "جيمناي" in tx:
                webbrowser.open("https://gemini.google.com/app")
                os.system("say 'Gemini'")
            elif "يوتيوب" in tx:
                webbrowser.open("https://www.youtube.com")
            elif "كاميرا" in tx:
                cap = cv2.VideoCapture(0)
                os.system("say 'Camera ON'")
                while True:
                    ret, f_cam = cap.read()
                    cv2.imshow("Camera", f_cam)
                    if cv2.waitKey(1) == 27: break
                cap.release()
                cv2.destroyAllWindows() 
            elif "طفي النت" in tx:
                os.system("networksetup -setairportpower en0 off")
            elif "شغل النت" in tx:
                os.system("networksetup -setairportpower en0 on")
            elif "وقف قوم" in tx or "طفي قوم" in tx:
                break

            elif "open" in txn:
                ap = txn.replace("open ", "").strip()
                os.system(f"open -a '{ap}'")
                os.system(f"say 'opening {ap}'")
            elif "kill" in txn:
                fo = txn.replace("kill ", "").strip()
                # تحديد مسار سطح المكتب
                dp1 = os.path.expanduser(f"~/Desktop/{fo}")
                
                if os.path.exists(dp1):
                    if os.path.isdir(dp1):
                        shutil.rmtree(dp1)
                        os.system(f"say 'folder {fo} killed from desktop'")
                    else:
                        os.system(f"say 'this is a file, not a folder'")
                else:
                    os.system(f"say 'folder not found on desktop'")

            elif "remove" in txn:
                fl = txn.replace("remove ", "").strip()
                dp = os.path.expanduser(f"~/Desktop/{fl}")
                
                if os.path.exists(dp):
                    if os.path.isfile(dp):
                        os.remove(dp)
                        os.system(f"say 'file {fl} deleted from desktop'")
                else:
                    os.system("say 'file not found on desktop'")
except Exception as e:
    print(f"System Error: {e}")