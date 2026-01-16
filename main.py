import tkinter as tk
from screeninfo import get_monitors
import math


root = tk.Tk()
root.title("Output Calculator")
root.configure(background="#42340c")
root.minsize(900,700)

screenx = get_monitors()[0].width
screeny = get_monitors()[0].height

root.geometry(f"{math.floor(screenx*0.33)}x{math.floor(screeny*0.33)}+{math.floor(screenx*0.25)}+{math.floor(screeny*0.05)}")

tk.Label(root, text="Satisfactory Output Calculator", font = ("Impact", 25), background = "#42340c", fg = "white").pack()
tk.Label(root, text="By Dan and John", background = "#42340c", fg = "white").pack()

tk.Text(root, height = 1, width = 20, bg = "black", fg = "white").pack()












root.mainloop()