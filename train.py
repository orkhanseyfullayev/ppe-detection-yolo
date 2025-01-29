from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8l.pt")
    model.train(data="dataset/dataset.yaml", epochs=50)  # Using a local dataset path