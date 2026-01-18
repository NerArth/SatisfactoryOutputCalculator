import tkinter as tk
import tkinter.font as tkfont
from screeninfo import get_monitors
import math
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Satisfactory Output Calculator")
root.configure(background="#42340c")

_bg_path = "background.png"
try:
	_bg_img = ImageTk.PhotoImage(Image.open(_bg_path))
	_background_label = tk.Label(root, image=_bg_img)
	_background_label.image = _bg_img
	_background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:
	pass

root.minsize(900,700)

screenx = get_monitors()[0].width
screeny = get_monitors()[0].height

root.geometry(f"{math.floor(screenx*0.33)}x{math.floor(screeny*0.33)}+{math.floor(screenx*0.25)}+{math.floor(screeny*0.05)}")

f = tkfont.Font(family='Arial', size=18, weight='bold', underline=1)
parameters = tk.Label(root, text="Parameters", font=f, background="#131313", fg="#FFFFFF")
parameters.place(relx=0.0, rely=0.0, anchor="nw")

desired_item = tk.Label(root, text="Desired item:", font=('Arial', 12, 'bold'), background="#131313", fg="white")
desired_item.place(relx=0.0, rely=0.06, anchor="nw")

input1 = tk.Text(root, height = 1, width = 20, bg = "black", fg = "white")
input1.place(relx=0.12, rely=0.06, anchor="nw")

desired_output = tk.Label(root, text="Desired output i/min:", font=('Arial', 12, 'bold'), background="#1A1A1A", fg="white")
desired_output.place(relx=0.34, rely=0.06, anchor="nw")

input2 = tk.Text(root, height = 1, width = 20, bg = "black", fg = "white")
input2.place(relx=0.53, rely=0.06, anchor="nw")









root.mainloop()