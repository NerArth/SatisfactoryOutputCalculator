import tkinter as tk
from screeninfo import get_monitors
import math


root = tk.Tk()
root.title("Output Calculator")
root.configure(background="#42340c")
root.minsize(600,400)

screenx = get_monitors()[0].width
screeny = get_monitors()[0].height

root.geometry(f"{math.floor(screenx*0.33)}x{math.floor(screeny*0.33)}+{math.floor(screenx*0.33)}+{math.floor(screeny*0.33)}")













root.mainloop()