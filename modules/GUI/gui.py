#============ Imports ============#

import customtkinter
from classes.log_interface import LogInterface
import time
import threading

#============ App ============#

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#============ Global Variables ============#

print("App Created")

log_screen = LogInterface(app)
log_screen.set_screen_size(300, 300)

#============ Functions ============#


def tst_button_click():
    log_screen.add_line(f"Test Button Clicked at {time.strftime('%H:%M:%S')}")

app.geometry("400x450")
app.title("Arknights-PRTS")

button = customtkinter.CTkButton(master=app, text="Test Button", command=tst_button_click)
button.place(x=10, y=400)


app.mainloop()