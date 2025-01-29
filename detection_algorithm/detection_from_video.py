import cv2
from ultralytics import YOLO
import numpy as np

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(80, 3), dtype="uint8")

def enhance_image(image):
    alpha = 1.1  # Contrast adjustment
    beta = 15    # Brightness boost
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    enhanced_image = cv2.GaussianBlur(enhanced_image, (3, 3), 0)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    enhanced_image = cv2.filter2D(enhanced_image, -1, kernel)
    return enhanced_image

model_path = r"C:/Users/model.pt"
video_path = r"C:/Users/video.mp4"

model = YOLO(model_path)
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    enhanced_frame = enhance_image(frame.copy())
    
    rgb_img = cv2.cvtColor(enhanced_frame, cv2.COLOR_BGR2RGB)
    results = model.track(rgb_img, persist=True, verbose=False)
    labels = results[0].names

    for i in range(len(results[0].boxes)):
        x1, y1, x2, y2 = results[0].boxes.xyxy[i]
        score = results[0].boxes.conf[i]
        label = results[0].boxes.cls[i]
        obj_id = results[0].boxes.id[i]
        x1, y1, x2, y2, score, label, obj_id = int(x1), int(y1), int(x2), int(y2), float(score), int(label), int(obj_id)
        name = labels[label]

        if score < 0.65:
            continue

        color = [int(c) for c in COLORS[label]]
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        text = f"{name} {score*100:.1f}%"
        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(frame, (x1, y1 - text_height - 5), (x1 + text_width, y1), color, -1)
        cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Detection Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()