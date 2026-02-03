import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk
from screeninfo import get_monitors
import math
from PIL import Image, ImageTk
import calculator

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
	print("Background image not found")
	pass

# Window Settings
root.minsize(900,700) # can't be resized smaller than this
screenx = get_monitors()[0].width
screeny = get_monitors()[0].height

root.geometry(
	f"{math.floor(screenx * 0.33)}x{math.floor(screeny * 0.33)}+" # initial size
	f"{math.floor(screenx * 0.25)}+{math.floor(screeny * 0.05)}" # initial position
)

f = tkfont.Font(family='Arial', size=18, weight='bold', underline=1) # default font

# Controls Definitions
## Parameters Section
parameters = tk.Label(root, text="Parameters", font=f, background="#131313", fg="#FFFFFF")
parameters.place(relx=0.0, rely=0.0, anchor="nw")

### Parameters Inputs ("The Form")
desired_item = tk.Label(root, text="Desired item:", font=('Arial', 12, 'bold'), background="#131313", fg="white")
desired_item.place(relx=0.0, rely=0.06, anchor="nw")

desired_item_data = calculator.Calculator().getItemNames()

desired_item_field = ttk.Combobox(root, values = desired_item_data, state="normal", width=20)
desired_item_field.set("Input item")
desired_item_field.place(relx=0.12, rely=0.06, anchor="nw")

desired_outputrate = tk.Label(root, text="Desired output i/min:", font=('Arial', 12, 'bold'), background="#1A1A1A", fg="white")
desired_outputrate.place(relx=0.34, rely=0.06, anchor="nw")

desired_outputrate_field = tk.Text(root, height = 1, width = 20, bg = "black", fg = "white")
desired_outputrate_field.place(relx=0.53, rely=0.06, anchor="nw")

##Submit button
button = tk.Button(root, text="Submit", bg="#222222", fg="white")
button.place(relx=0.80, rely=0.06, anchor="ne")

##Result field

result = canvas = tk.Canvas(root, bg="white", width=600, height=300)
result.place(relx=0.5, rely=0.55, anchor="center")

frame = "metal.png"

try:
	img = ImageTk.PhotoImage(Image.open(frame).resize((620, 25)))	
except Exception:
	print("Frame image not found")
	exit()
frame_label_top = tk.Label(root, image=img, borderwidth=0)
frame_label_bottom = tk.Label(root, image=img, borderwidth=0)
frame_label_top.place(relx=0.50, rely=0.32, anchor="center")
frame_label_bottom.place(relx=0.50, rely=0.77, anchor="center")


# TODO: Make the button calculate the results

# Calculation Result Section
# TODO: Make code for the image to appear on the side frames
# The black "screen" area needs to have:
# - vertical and horizontal scrollbars at minimum;
# - ideally needs to be pannable with drag click;
# - zooming would be a bonus;


# Run
root.mainloop()