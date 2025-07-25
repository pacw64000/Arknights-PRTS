""""
Mouse handling module

its going to take a starting position and an ending position and then trace a path generated based on a bezier curve
and then move the mouse along that path while holding the left mouse button down

scroll ui pos
(1755, 218) to (1126, 179)

confirm level pos
(1740, 794)

select level, 3 level format pos
(621, 304)
(621, 491)
(618, 667)

select level, 2 level format pos
(584, 570)
(587, 389)

select level, 1 level format pos
(626, 482)

Select Level layout image Pos
(1563, 574)


functions:
    move_mouse(start_pos, end_pos, duration)
    scroll_side_to_side(start_pos, end_pos, duration)
    select_level(level_select, level_format)
    select_level_layout()

"""

import mouse
import time
import threading
import bezier
import numpy as np
import keyboard
import pyautogui
import os
from datetime import datetime


class MouseHandler:
    def __init__(self):
        pass

    def move_mouse(self, start_pos, end_pos, duration=1.0):
        """Move mouse from start position to end position over a specified duration"""
        # Define control points for Bezier curve
        control_points = np.array([start_pos, end_pos])
        
        # Create Bezier curve
        curve = bezier.Curve(control_points, degree=1)
        
        # Generate points along the curve
        num_points = 100
        t = np.linspace(0, 1, num_points)
        points = curve.evaluate_multi(t).T
        
        # Move mouse along the curve
        for point in points:
            pyautogui.moveTo(point[0], point[1])
            time.sleep(duration / num_points)
            if keyboard.is_pressed('esc'):
                break

    def scroll_side_to_side(self, start_pos, end_pos, duration=1.0):
        """Scroll from start position to end position and back over a specified duration"""
        # Move mouse to start position
        pyautogui.moveTo(start_pos[0], start_pos[1])
        
        # Calculate distance to scroll
        distance = end_pos[0] - start_pos[0]
        
        # Calculate scroll amount per step
        num_steps = 100
        step_size = distance / num_steps
        
        # Scroll side to side
        for i in range(num_steps):
            pyautogui.moveRel(step_size, 0)
            time.sleep(duration / num_steps)
            if keyboard.is_pressed('esc'):
                break
        for i in range(num_steps):
            pyautogui.moveRel(-step_size, 0)
            time.sleep(duration / num_steps)
            if keyboard.is_pressed('esc'):
                break

    def select_level(self, level_select, level_format):
        """Select a level by clicking on it"""
        # Check if level format matches
        match level_format:
            case 1:
                match level_select:
                    case 1:
                        pyautogui.click(626, 482)
            case 2:
                match level_select:
                    case 1:
                        pyautogui.click(584, 570)
                    case 2:
                        pyautogui.click(587, 389)
            case 3:
                match level_select:
                    case 1:
                        pyautogui.click(621, 304)
                    case 2:
                        pyautogui.click(621, 491)
                    case 3:
                        pyautogui.click(618, 667)
        time.sleep(5)
        pyautogui.click(1740, 794)

    def select_level_layout(self):
        pyautogui.click(1563, 574)

