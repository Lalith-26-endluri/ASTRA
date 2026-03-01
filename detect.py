from ultralytics import YOLO
import cv2

# Load YOLOv8 model once
model = YOLO("yolov8n.pt")

def detect_crowd(frame):
    results = model(frame)
    crowd_count = 0

    for r in results:
        for box in r.boxes:
            crowd_count += 1

    return crowd_count, results
