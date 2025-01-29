import os
import cv2
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

def apply_synthetic_effects(image):
    rows, cols, _ = image.shape
    fog_layer = np.random.normal(loc=200, scale=60, size=(rows, cols, 1)).astype(np.uint8)
    fog_layer = cv2.merge([fog_layer, fog_layer, fog_layer])
    fogged_image = cv2.addWeighted(image, 0.7, fog_layer, 0.3, 0)

    brightness_factor = 1.2
    brightness_offset = 40
    enhanced_image = cv2.convertScaleAbs(fogged_image, alpha=brightness_factor, beta=brightness_offset)
    return enhanced_image

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_name = f"synthetic_{file_name}"
            output_file_path = os.path.join(output_folder, output_file_name)

            image = cv2.imread(input_file_path)
            if image is None:
                print(f"Failed to load {file_name}.")
                continue

            processed_image = apply_synthetic_effects(image)
            cv2.imwrite(output_file_path, processed_image)
            print(f"{output_file_name} successfully processed and saved.")

input_directory = "C:\\Users\\photos-in" 
output_directory = "C:\\Users\\photos-out"

process_images(input_directory, output_directory)
