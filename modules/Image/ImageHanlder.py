"""
Level Selector image Pos
(378, 122) to (911, 879)

Level layout image Pos
(235, 84) to (1687, 907)

"""


import pyautogui
import os
from datetime import datetime
import cv2
import numpy as np
import shutil

class ImageHandler:
    def __init__(self):
        # Create necessary directories if they don't exist
        self.base_dir = "Images"
        self.temp_dir = os.path.join(self.base_dir, "temp")
        self.processed_dir = os.path.join(self.base_dir, "processed")
        
        for dir_path in [self.base_dir, self.temp_dir, self.processed_dir]:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    def capture_image(self, x, y, width, height):
        """Capture screenshot at specified coordinates"""
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{x}+{y}+{width}+{height}+{timestamp}.png"
        save_path = os.path.join(self.temp_dir, filename)
        screenshot.save(save_path)
        return save_path, filename

    def convert_to_grayscale(self, image_path):
        """Convert image to grayscale"""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        filename = os.path.basename(image_path)
        gray_filename = f"gray_{filename}"
        save_path = os.path.join(self.processed_dir, gray_filename)
        cv2.imwrite(save_path, gray)
        return save_path

    def resize_image(self, image_path, scale_percent):
        """Resize image by percentage"""
        img = cv2.imread(image_path)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        filename = os.path.basename(image_path)
        resized_filename = f"resized_{filename}"
        save_path = os.path.join(self.processed_dir, resized_filename)
        cv2.imwrite(save_path, resized)
        return save_path

    def copy_to_folder(self, image_path, destination_folder):
        """Copy image to specified folder"""
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        filename = os.path.basename(image_path)
        dest_path = os.path.join(destination_folder, filename)
        shutil.copy2(image_path, dest_path)
        return dest_path
