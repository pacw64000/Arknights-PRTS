import pyautogui
import keyboard
import mouse
import time
import os
from datetime import datetime

start_pos = None

def on_click(event):
    global start_pos
    try:
        if event.button == 'right' and event.event_type == 'down':
            start_pos = mouse.get_position()
    except AttributeError:
        pass  # Ignore events that don't have button or event_type attributes

def capture_image():    # Create Images directory if it doesn't exist            
    if not os.path.exists("Images/temp"):
        os.makedirs("Images/temp")            
    # Wait for right mouse button press            
    print("Click and drag to select area...")
    global start_pos
    start_pos = None
    mouse.hook(on_click)            
    print(start_pos)
    # Wait for mouse press
    while start_pos is None:
        time.sleep(0.1)
        if start_pos is not None:
            print(start_pos)

        if keyboard.is_pressed('esc'):
            mouse.unhook(on_click)
            return                 
    # Wait for mouse release            
    while mouse.is_pressed("right"):                
        time.sleep(0.1)            
    # Get end position            
    end_pos = mouse.get_position()    
    print(end_pos)        
    mouse.unhook(on_click)            
    # Calculate region            
    x = min(start_pos[0], end_pos[0])            
    y = min(start_pos[1], end_pos[1])            
    width = abs(end_pos[0] - start_pos[0])            
    height = abs(end_pos[1] - start_pos[1])            
    # Capture screenshot            
    screenshot = pyautogui.screenshot(region=(x, y, width, height))            
    # Generate filename with position and timestamp            
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")            
    filename = f"{x}+{y}+{width}+{height}+{timestamp}.png"            
    save_path = os.path.join("Images/temp", filename)            
    screenshot.save(save_path)            
    print(f"Image saved as: {filename}")    
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
































