import tkinter as tk
import tkinter.font as tkfont
from screeninfo import get_monitors
import math


root = tk.Tk()
root.title("Satisfactory Output Calculator")
root.configure(background="#42340c")
root.minsize(900,700)

screenx = get_monitors()[0].width
screeny = get_monitors()[0].height

root.geometry(f"{math.floor(screenx*0.33)}x{math.floor(screeny*0.33)}+{math.floor(screenx*0.25)}+{math.floor(screeny*0.05)}")

f = tkfont.Font(family='Arial', size=18, weight='bold', underline=1)
parameters = tk.Label(root, text="Parameters", font=f, background="#42340c", fg="#B4B4B4")
parameters.place(relx=0.0, rely=0.0, anchor="nw")

desired_item = tk.Label(root, text="Desired item:", font=('Arial', 12, 'bold'), background="#42340c", fg="white")
desired_item.place(relx=0.0, rely=0.06, anchor="nw")

input1 = tk.Text(root, height = 1, width = 20, bg = "black", fg = "white")
input1.place(relx=0.12, rely=0.06, anchor="nw")













root.mainloop()