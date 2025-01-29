import cv2
import numpy as np
from ultralytics import YOLO

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(80, 3), dtype="uint8")

def enhance_image(image):
    alpha = 1.1
    beta = 15
    enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    enhanced_image = cv2.GaussianBlur(enhanced_image, (3, 3), 0)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    enhanced_image = cv2.filter2D(enhanced_image, -1, kernel)
    return enhanced_image

model_path = r"C:/Users/best.pt"
image_path = r"C:/Users/photo.jpg"

model = YOLO(model_path)
img = cv2.imread(image_path)
if img is None:
    print("Image could not be loaded. Please check the path.")
    exit()

max_width = 1500
max_height = 1000
height, width = img.shape[:2]
if width > max_width or height > max_height:
    scaling_factor = min(max_width / width, max_height / height)
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

enhanced_img = enhance_image(img.copy())

def run_detection(img, model, window_name):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(rgb_img, verbose=False)
    labels = results[0].names

    for i in range(len(results[0].boxes)):
        x1, y1, x2, y2 = results[0].boxes.xyxy[i]
        score = results[0].boxes.conf[i]
        label = results[0].boxes.cls[i]
        x1, y1, x2, y2, score, label = int(x1), int(y1), int(x2), int(y2), float(score), int(label)
        name = labels[label]

        if score < 0.5:
            continue

        print(f"Detected: {name}, Score: {score*100:.2f}%, Box: ({x1}, {y1}, {x2}, {y2})")

        color = [int(c) for c in COLORS[label]]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

        text = f"{name} {score*100:.1f}%"
        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(img, (x1, y1 - text_height - 5), (x1 + text_width, y1), color, -1)
        cv2.putText(img, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow(window_name, img)

run_detection(img.copy(), model, "Detection on Original Image")
run_detection(enhanced_img.copy(), model, "Detection on Enhanced Image")

cv2.waitKey(0)
cv2.destroyAllWindows()