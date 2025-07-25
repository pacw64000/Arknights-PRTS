import os
import cv2
import shutil
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from modules.Image.ImageHanlder import ImageHandler

def process_images():
    # Initialize ImageHandler
    img_handler = ImageHandler()

    # Check if original directory exists
    original_dir = "./Images/original"
    if not os.path.exists(original_dir):
        print(f"Error: {original_dir} does not exist")
        return

    # Define size folders and offset subfolders
    size_folders = ['520x170', '540x190', '560x220']
    offset_folders = ['x10px_offset', 'x20px_offset', 'x30px_offset', 'x40px_offset']

    def process_directory(current_dir, relative_path=""):
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            
            # If it's a directory, process it recursively
            if os.path.isdir(item_path):
                process_directory(item_path, os.path.join(relative_path, item))
            
            # If it's an image file, process it
            elif item.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"Processing: {item}")
                
                # Process for each size folder
                for size_folder in size_folders:
                    # Parse dimensions from folder name
                    width, height = map(int, size_folder.split('x'))
                    
                    # Read and resize the image
                    img = cv2.imread(item_path)
                    resized_img = cv2.resize(img, (width, height))
                    
                    
                    
                    # Process for each offset folder
                    for offset_folder in offset_folders:
                        # Parse offset from folder name
                        offset = int(offset_folder.split('px_')[0].replace('x', ''))
                        
                        # Create directory path maintaining original structure
                        processed_path = os.path.join("./Images/processed", size_folder, 
                                                    offset_folder, relative_path)
                        os.makedirs(processed_path, exist_ok=True)
                        
                        # Create offset version of the image with padding
                        offset_img = cv2.copyMakeBorder(resized_img, 0, 0, offset, 0, 
                                                      cv2.BORDER_CONSTANT, value=[0, 0, 0])
                        # Crop the image to maintain original dimensions
                        offset_img = offset_img[:, offset:offset+width, :]
                        # Create grayscale version of the image
                        gray_img = cv2.cvtColor(offset_img, cv2.COLOR_BGR2GRAY)
                        # Save grayscale image
                        gray_save_path = os.path.join("./Images/processed", size_folder, offset_folder,
                                                    "training_images_grayscale", relative_path.replace('training_images/', ''))
                        os.makedirs(gray_save_path, exist_ok=True)
                        cv2.imwrite(os.path.join(gray_save_path, item), gray_img)
                        print(f"Processed grayscale {item} for {size_folder}/{offset_folder}")
                        
                        # Save processed image
                        save_path = os.path.join(processed_path, item)
                        cv2.imwrite(save_path, offset_img)
                        print(f"Processed {item} for {size_folder}/{offset_folder}")

    # Start processing from the original directory
    process_directory(original_dir)

def main():
    process_images()

if __name__ == "__main__":
    main()
