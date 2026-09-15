import pyautogui
import time
v = input("l or r: ")
# انتظر 5 ثوانٍ قبل البدء لتتمكن من فتح النافذة المطلوبة
time.sleep(5)
if v == "l":
    while True:
        pyautogui.click(button='left')
        time.sleep(0.02)
    print("RUNNING")
if v == "r":
    while True:
        pyautogui.click(button='right')
        time.sleep(0.02)
    print("RUNNING")