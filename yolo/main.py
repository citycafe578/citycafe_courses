# 資料來源 : https://www.youtube.com/watch?v=tMwyxKttZd0

# 建立虛擬環境
# pip install "ultralytics<=8.3.40"
# pip install opencv-contrib-python
# pip install labelImg
# yolo task=detect mode=predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"

from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 或你自己訓練的模型

# 來源 0 表示預設 webcam，如果你接 drone 可放 RTSP 或 MJPEG URL
model.predict(source=0, show=True)