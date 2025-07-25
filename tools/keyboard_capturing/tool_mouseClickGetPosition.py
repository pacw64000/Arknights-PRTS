""""
This tool is used to capture the position of a mouse click.
It is used to get the position of the mouse click for the mouse module.
"""
import mouse
import time

def on_click(event):
    try:
        if event.button == 'left' and event.event_type == 'down':
            pos = mouse.get_position()
            print(f"Mouse clicked at {pos}")
    except AttributeError:
        pass  # Ignore events that don't have button or event_type attributes

def main():
    print("Click on the screen to capture the position...")
    mouse.hook(on_click)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()