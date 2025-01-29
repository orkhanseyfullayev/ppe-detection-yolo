# PPE Detection Using YOLOv8

This repository contains an AI-based Personal Protective Equipment (PPE) detection system using **YOLOv8**. The system is capable of detecting safety gear such as helmets, vests, and glasses in images and videos.

---

## Features
- **Real-time object detection** for PPE equipment.
- **Custom YOLOv8 model training** on an enhanced dataset.
- **Image preprocessing** for better accuracy.
- **Synthetic data generation** to improve dataset diversity.
- **Detection on images and videos** with visualization.

---

## Installation

Ensure you have Python 3.7+ installed, then install dependencies:

```bash
pip install ultralytics opencv-python numpy
```

---

## Dataset
This project uses a dataset containing PPE images and annotations in YOLO format. The dataset includes real and synthetically generated images to improve model robustness.

---

## Training the Model
To train the model on the dataset, run:
```bash
python train.py --epochs 100 --batch 16 --imgsz 640
```

---

## Running Detection
To perform PPE detection on an image:

```bash
python detection_algorithm/from_photo.py --source path_to_image.jpg
```
For video detection:

```bash
python detection_algorithm/from_video.py --source path_to_video.mp4
```

---

## Project Structure

```
📂 ppe-detection-yolo
├── dataset/
│   ├── images/
│   ├── labels/
│   ├── synthetic_data_generator/
│   │   ├── generate_synthetic_images.py
│   │   ├── rename_txt_files.py
│   ├── dataset.yaml
│   ├── README.md
├── detection_algorithm/
│   ├── detection_from_photo.py
│   ├── detection_from_video.py
├── LICENSE
├── train.py
├── README.md

```

---

## Conclusion
This project successfully implements **YOLOv8** for detecting Personal Protective Equipment (PPE) in images and videos. The model is trained on an enriched dataset, including synthetic images to improve detection accuracy in diverse environments. Image preprocessing techniques enhance detection precision, making the system robust against lighting variations and noise. The system provides reliable real-time detection and can be adapted for safety compliance monitoring in construction sites, factories, and hazardous work environments.

---

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share it.

---

## Author
Developed by **[Orkhan Seyfullayev](https://github.com/orkhanseyfullayev)**. For queries, reach out via email or GitHub.



