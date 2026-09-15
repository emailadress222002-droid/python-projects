import cv2, mediapipe as mp, os

cap = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose.Pose()

while True:
    res, frame = cap.read()
    if not res:
        break
    results = mp_pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.pose_landmarks: 
        os.system("say 'Get out human'")
    #...
    cv2.imshow('rec', frame)
    if cv2.waitKey(1) == 27: break