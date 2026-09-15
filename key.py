import cv2, numpy as np
cap = cv2.VideoCapture(0)
while cap.isOpened():
   r, f = cap.read()
   mask = cv2.inRange(cv2.cvtColor(f, cv2.COLOR_BGR2HSV), (11, 150, 150), (25, 255, 255)) | \
           cv2.inRange(cv2.cvtColor(f, cv2.COLOR_BGR2HSV), (26, 100, 100), (35, 255, 255))
   cv2.imshow('cam83', cv2.bitwise_and(f, f, mask=mask))
   key = cv2.waitKey(1) & 0xFF
   if key == ord("÷"):
      break
cap.release()
cv2.destroyAllWindows()
