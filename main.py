import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk
from screeninfo import get_monitors
import math
from PIL import Image, ImageTk, ImageOps, ImageTransform
import calculator

root = tk.Tk()
root.title("Satisfactory Output Calculator")
root.configure(background="#42340c")

# Custom Functions
## Handlers
def handleImageOpen(image_path, flip_horizontal = False, size = None):
	"""
	Opens an image from `image_path`, returns it as PhotoImage (tkinter)

	Accepts optional `flip_horizontal` to flip the image horizontally
	Accepts optional `size` to stretch image to the given width and height
	"""
	def flip(image):
		"""
		Helper function to flip the image horizontally
		Expects PIL Image as input, returns PIL Image
		"""
		return ImageOps.mirror(image)

	try:
		_img = Image.open(image_path) # PIL Image

		if flip_horizontal:
			_img = flip(_img)
		
		# TODO: Add support to make the image crop and tile as required for specified size
		# 
		# The transform method will be important for this, because right now we are just
		# using it to stretch the image, but we can write code to make it crop and tile
		if size:
			_iw, _ih = _img.size
			_w, _h = size
			_img = _img.transform(size, Image.Transform.QUAD, (0, 0, 0, _ih, _iw, 0, _iw, _ih))

		# tkinter PhotoImage, what we want to return
		# remember this has to be assigned to a variable
		_img = ImageTk.PhotoImage(_img)
		return _img
	except Exception as e:
		print("Could not handle image at path: ", image_path)
		print("Unhandled exception: ", e)
		return None
		
# Load background image
_bg_img = handleImageOpen("background.png")
try:
	_background_label = tk.Label(root, image=_bg_img)
	_background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
	# print("Background image not found")
	print("Unhandled exception when loading background image: ", e)
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

## Submit button
button = tk.Button(root, text="Submit", bg="#222222", fg="white")
button.place(relx=0.80, rely=0.06, anchor="ne")

## Visual area for results
# We place a container to make it easier to have full control
# of the canvas without things floating away from each other.
res_size = (600, 400) # XY absolute size in pixels
res_size_rel = (0.80, 0.60) # XY size % of root
result_container = tk.Frame(root, bg="#131313")
# result_container.place(relx=0.5, rely=0.5, relwidth=res_size_rel[0], relheight=res_size_rel[1], anchor="center")
result_container.place(relx=0.5, rely=0.5, width=res_size[0], height=res_size[1], anchor="center")

result_canvas = tk.Canvas(result_container, bg="#131313")
# result_canvas.place(relx=0.5, rely=0.5, relwidth=res_size_rel[0], relheight=res_size_rel[1], anchor="center")
result_canvas.place(relx=0.5, rely=0.5, width=res_size[0], height=res_size[1], anchor="center")

frame_top = handleImageOpen("img/ui/screenframe_topcent.png", size=(res_size[0]-32,16))
frame_right = handleImageOpen("img/ui/screenframe_midleft.png", flip_horizontal=True, size=(16,res_size[1]))
frame_bottom = handleImageOpen("img/ui/screenframe_botcent.png", size=(res_size[0]-32,16))
frame_left = handleImageOpen("img/ui/screenframe_midleft.png", size=(16,res_size[1]))

# NOTE: deprecated implementation
# _w, _h = frame_top.size
# applied_frame_top = frame_top.transform((_w*20,_h), Image.Transform.QUAD, (0, 0, 0, _h, _w, 0, _w, _h))
# frame_label_top = tk.Label(root, image=ImageTk.PhotoImage(applied_frame_top), borderwidth=0)

# Clockwise assignment
frame_label_top = tk.Label(result_container, image=frame_top, borderwidth=0)
frame_label_right = tk.Label(result_container, image=frame_right, borderwidth=0)
frame_label_bottom = tk.Label(result_container, image=frame_bottom, borderwidth=0)
frame_label_left = tk.Label(result_container, image=frame_left, borderwidth=0)

frame_label_top.place(relx=0.5, rely=0, anchor="n")
frame_label_right.place(relx=1.0, rely=0.5, anchor="e")
frame_label_bottom.place(relx=0.5, rely=1.0, anchor="s")
frame_label_left.place(relx=0, rely=0.5, anchor="w")



# TODO: Make the button calculate the results

# Calculation Result Section
# TODO: Make code for the image to appear on the side frames
# The "screen" area needs to have:
# - vertical and horizontal scrollbars at minimum;
# - ideally needs to be pannable with drag click;
# - zooming would be a bonus;


# Run
root.mainloop()