import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#DirectShow 後端  windows內建影像撥放器的API

while True:
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.resize(frame, (1920, 1080))

    cv2.imshow("test", frame)
    if(cv2.waitKey(1) == ord('q')):
        break
    

cap.release()
cv2.destroyAllWindows()