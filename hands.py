import cv2, mediapipe as mp, pyautogui as pd
h = mp.solutions.hands.Hands(max_num_hands=1)
sw, sh = pd.size()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    r, img = cap.read()
    if not r: break
    img = cv2.flip(img, 1)
    res = h.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for lm in res.multi_hand_landmarks:
            p = lm.landmark
            pd.moveTo(p[8].x * sw, p[8].y * sh, _pause=False)
            if all(p[i].y > p[i-2].y for i in [8, 12, 16, 20]):
                pd.click(); pd.sleep(0.2)
    cv2.imshow("M2", img)
    if cv2.waitKey(1) == 27: break
    cap.release()
