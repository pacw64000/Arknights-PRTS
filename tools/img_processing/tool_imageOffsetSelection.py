import os
import cv2
import shutil
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from modules.Image.ImageHanlder import ImageHandler

def process_images(image_path, top, bottom, left, right):
    """
    Process image by creating a selection box based on offsets and save results
    Args:
        image_path (str): Path to the source image
        top (int): Offset from top edge
        bottom (int): Offset from bottom edge
        left (int): Offset from left edge
        right (int): Offset from right edge
    Returns:
        tuple: (path to image with selection box, path to cropped selection)
    """
    # Initialize ImageHandler
    img_handler = ImageHandler()

    # Check if image exists
    if not os.path.exists(image_path):
        print(f"Error: Image at {image_path} does not exist")
        return None, None

    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return None, None

    # Get image dimensions
    height, width = img.shape[:2]

    # Validate coordinates
    if left >= width or top >= height or right >= width or bottom >= height:
        print(f"Error: Invalid coordinates - image dimensions are {width}x{height}")
        return None, None

    # Calculate selection box coordinates
    x1 = left
    y1 = top
    x2 = width - right
    y2 = height - bottom

    # Validate selection box dimensions
    if x2 <= x1 or y2 <= y1:
        print("Error: Invalid selection box dimensions")
        return None, None

    # Create a copy of original image with selection box
    img_with_box = img.copy()
    cv2.rectangle(img_with_box, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Crop the selected region
    selected_region = img[y1:y2, x1:x2]

    # Verify the selected region is not empty
    if selected_region.size == 0:
        print("Error: Selected region is empty")
        return None, None

    # Create temp directory if it doesn't exist
    temp_dir = os.path.join("Images", "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # Generate filenames
    base_filename = os.path.splitext(os.path.basename(image_path))[0]
    box_filename = f"{base_filename}_with_box.png"
    crop_filename = f"{base_filename}_cropped.png"
    
    # Save or replace both images
    box_path = os.path.join(temp_dir, box_filename)
    crop_path = os.path.join(temp_dir, crop_filename)
    if os.path.exists(box_path):
        os.remove(box_path)
    if os.path.exists(crop_path):
        os.remove(crop_path)
    
    # Save images with error checking
    if not cv2.imwrite(box_path, img_with_box):
        print("Error: Failed to save image with box")
        return None, None
    if not cv2.imwrite(crop_path, selected_region):
        print("Error: Failed to save cropped image")
        return None, None

    return box_path, crop_path


def main():
    # Example usage
    image_path = "./Images/processed/520x170/x10px_offset/training_images/Casters/Goldenglow.png"
    left, top, right, bottom = 290, 90, 120, 50
    box_path, crop_path = process_images(image_path, top, bottom, left, right)
    print(f"Image with box saved at: {box_path}")
    print(f"Cropped image saved at: {crop_path}")

if __name__ == "__main__":
    main()
