# Dataset Information

This dataset is used for training a **YOLOv8 model** to detect Personal Protective Equipment (PPE), including:
- Helmets (white, blue, yellow, red, head)
- Vests
- Masks
- Glasses

## Structure
The dataset consists of:
- **Images**: Collected and labeled images for training and validation.
- **Labels**: YOLO format annotation files.
- **Dataset Configuration**: `dataset.yaml` file specifying class names and paths.

## Download
Due to large file size, the dataset is hosted externally. You can download it from the following link:
🔗 [Download Dataset](https://your-dataset-link.com)

## **Synthetic Data Generation**  

To enhance the dataset, **synthetic data generation techniques** were applied. Initially, the dataset contained **1699 real images**, which were expanded to **3398 images** through augmentation.  

The **synthetic data generation process** includes:  
- **Fog and brightness effects** to simulate real-world conditions.  
- **Automatic renaming of label files** to maintain consistency.  

The scripts used for synthetic data generation can be found in the [synthetic_data_generator](https://github.com/orkhanseyfullayev/ppe-detection-yolo/tree/main/dataset/synthetic_data_generator) directory.


## Usage
After downloading, place the extracted dataset in this directory:
```
📂 dataset
├── images/        # Training and validation images
├── labels/        # YOLO format labels
├── dataset.yaml   # Configuration file
```

Make sure `dataset.yaml` is correctly configured before training.

## Notes
- This dataset was prepared for PPE detection in industrial environments.
- Data augmentation techniques were applied to improve model robustness.
- If you use this dataset, please provide attribution.

---

📌 **For any issues or updates, refer to the main repository.** 🚀
