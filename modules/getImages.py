import pyautogui
import os

class ImageGrabber:
    def __init__(self):        # Create temp directory if it doesn't exist
        self.temp_dir = "./Images/temp"
        if not os.path.exists(self.temp_dir):            os.makedirs(self.temp_dir)
    def capture_region(self, pos_x, pos_y, size_x, size_y, filename):        """
        Capture a specific region of the screen and save it to temp directory        
        Args:            pos_x (int): X coordinate of top-left corner
            pos_y (int): Y coordinate of top-left corner            size_x (int): Width of region to capture
            size_y (int): Height of region to capture
            filename (str): Name to save the image as                Returns:
            str: Path to saved image        """
        # Capture the specified region        screenshot = pyautogui.screenshot(region=(pos_x, pos_y, size_x, size_y))
                # Generate full path for saving
        save_path = os.path.join(self.temp_dir, filename)        
        # Save the image        screenshot.save(save_path)
        
        return save_path

















