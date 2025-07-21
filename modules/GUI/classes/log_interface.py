import customtkinter
import time
import os
from datetime import datetime

class LogInterface:
    def __init__(self, master):
        self.width = 300
        self.height = 300
        self.content = []
        self.buffer_size = 1000
        self.auto_scroll = True
        self.log_directory = "./Logs"
        
        # Initialize main text widget instead of scrollable frame
        self.master = master
        self.log_screen = customtkinter.CTkTextbox(master, width=self.width, height=self.height)
        self.log_screen.place(x=10, y=10)
        self.log_screen.configure(state="disabled")  # Make it read-only
        
        # Create logs directory if it doesn't exist
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)
            
        # Create new log file
        self.current_file = os.path.join(self.log_directory, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        # Bind scroll events
        self.log_screen.bind("<MouseWheel>", self.on_scroll)
        
    def on_scroll(self, event):
        if self.log_screen.yview()[1] < 1.0:
            self.auto_scroll = False
        else:
            self.auto_scroll = True
            
        # Load previous content when scrolling to top
        if self.log_screen.yview()[0] <= 0:
            self.load_earlier_logs()

    def load_earlier_logs(self):
        try:
            with open(self.current_file, 'r') as f:
                all_lines = f.readlines()
                current_content = self.log_screen.get("1.0", "end-1c").split('\n')
                if current_content[0]:  # If there's content
                    try:
                        idx = all_lines.index(current_content[0] + '\n')
                        new_lines = all_lines[max(0, idx-100):idx]
                        if new_lines:
                            self.log_screen.configure(state="normal")
                            self.log_screen.insert("1.0", ''.join(new_lines))
                            self.log_screen.configure(state="disabled")
                    except ValueError:
                        pass
        except Exception as e:
            print(f"Error loading earlier logs: {e}")

    def update_content(self, content):
        self.content = content[-self.buffer_size:]
        self.save_to_file(content)
        self.display_content()

    def clear_content(self):
        self.content = []
        self.log_screen.configure(state="normal")
        self.log_screen.delete("1.0", "end")
        self.log_screen.configure(state="disabled")
        self.auto_scroll = True

    def add_line(self, line):
        line_with_newline = f"{line}\n"
        self.content.append(line_with_newline)
        if len(self.content) > self.buffer_size:
            self.content = self.content[-self.buffer_size:]
        self.save_to_file([line_with_newline])
        
        # Update display
        self.log_screen.configure(state="normal")
        self.log_screen.insert("end", line_with_newline)
        self.log_screen.configure(state="disabled")
        
        if self.auto_scroll:
            self.log_screen.see("end")

    def save_to_file(self, lines):
        with open(self.current_file, 'a') as f:
            f.writelines(lines)

    def set_screen_size(self, width, height):
        self.width = width
        self.height = height
        self.log_screen.configure(width=width, height=height)

    def display_content(self):
        self.log_screen.configure(state="normal")
        self.log_screen.delete("1.0", "end")
        self.log_screen.insert("1.0", ''.join(self.content))
        self.log_screen.configure(state="disabled")
        if self.auto_scroll:
            self.log_screen.see("end")
