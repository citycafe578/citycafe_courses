import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
a = 1
phone_height = 16
real_distance = 50
focal = 2000 #筆電2000 桌機700

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)#
    frame = cv2.resize(frame, (1920, 1080))
    
    results = model(frame)

    # 開始處理資訊
    for result in results:
        boxes = result.boxes.xyxy
        class_ids = result.boxes.cls

        for i, box in enumerate(boxes):#
            class_id = int(class_ids[i])
            if class_id == 67:
                x1, y1, x2, y2 = map(int, box)
                phone_pixel = max(x2 - x1, y2 - y1)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                # d = (phone_pixel * real_distance) / phone_height #計算焦距
                d = (phone_height * focal) / phone_pixel #計算距離
                cv2.putText(frame, f"Phone, distance:{d}cm", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)


    cv2.imshow("YOLO Phone Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
