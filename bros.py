import cv2

url = "url"
c = cv2.VideoCapture(url)


fourcc = cv2.VideoWriter_fourcc(*'avc1')

o = cv2.VideoWriter('bros.mp4', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' ON THE VIDEO WINDOW to save.")

try:
    while True:
        r, f = c.read()
        if not r: 
            print("Connection lost!")
            break
        
        o.write(f)
        cv2.imshow('oppo live', f)
        

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
finally:
    
    c.release()
    o.release()
    cv2.destroyAllWindows()
    print("\n[SUCCESS] Video is now safe to open!")