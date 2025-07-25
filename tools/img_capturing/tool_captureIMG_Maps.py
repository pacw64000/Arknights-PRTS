"""
Level layout image Pos
(235, 84) to (1687, 907)

"""

import pyautogui
import keyboard
import mouse
import time
import os
from datetime import datetime
from PIL import Image

start_pos = None

def on_click(event):
    global start_pos
    try:
        if event.button == 'right' and event.event_type == 'down':
            start_pos = mouse.get_position()
    except AttributeError:
        pass  # Ignore events that don't have button or event_type attributes

def capture_image():    
    # Create Images directory if it doesn't exist            
    if not os.path.exists("Images/temp"):
        os.makedirs("Images/temp")            
    
    start_pos = (235, 84)
    end_pos = (1687, 907)
    
    # Calculate region            
    x = min(start_pos[0], end_pos[0])            
    y = min(start_pos[1], end_pos[1])            
    width = abs(end_pos[0] - start_pos[0])            
    height = abs(end_pos[1] - start_pos[1])            
    
    # Ensure width and height are at least 1 pixel
    width = max(1, width)
    height = max(1, height)
    
    try:
        # Capture screenshot            
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        
        # Convert to RGB mode to ensure compatibility
        screenshot = screenshot.convert('RGB')
        
        # Generate filename with position and timestamp            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")            
        filename = f"{x}+{y}+{width}+{height}+{timestamp}.png"            
        save_path = os.path.join("Images/temp", filename)            
        
        # Save with error handling
        screenshot.save(save_path, format='PNG')            
        print(f"Image saved as: {filename}")
    except Exception as e:
        print(f"Error capturing/saving image: {str(e)}")

def main():
    print("Press 'c' to capture, 'esc' to exit")    
    while True:        
        if keyboard.is_pressed('c'):            
            capture_image()            
            time.sleep(0.5)  # Prevent multiple captures        
        elif keyboard.is_pressed('esc'):            
            break

if __name__ == "__main__":
    main()
