# tkinter Widgets
Quick reference cheat sheet of tkinter widgets.
Links should all work but some may not be correct yet.

## Input & Display Widgets

These are the foundational components used to interact with or show data.

|Element|Description|
|---|---|
|[Label](https://www.tcl-lang.org/man/tcl8.6/TkCmd/label.htm)|Displays text or images. It is non-interactive.|
|[Button](https://www.tcl-lang.org/man/tcl8.6/TkCmd/button.htm)|A standard clickable button to trigger actions.|
|[Entry](https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm)|A single-line text field for user input.|
|[Text](https://www.tcl-lang.org/man/tcl8.6/TkCmd/text.htm)|A multi-line text area allowing for complex formatting and editing.|
|[Checkbutton](https://www.tcl-lang.org/man/tcl8.6/TkCmd/checkbutton.htm)|A toggle switch representing a boolean state (on/off).|
|[Radiobutton](https://www.tcl-lang.org/man/tcl8.6/TkCmd/radiobutton.htm)|Used to select one option from a predefined set.|
|[Scale](https://www.tcl-lang.org/man/tcl8.6/TkCmd/scale.htm)|A slider bar for selecting a numeric value from a range.|
|[Spinbox](https://www.tcl-lang.org/man/tcl8.6/TkCmd/spinbox.htm)| An entry field with "up" and "down" arrows to increment/decrement values.|

## Container & Layout Widgets
These widgets organize and group other elements within the UI.

|Element|Description|
|---|---|
|[Frame](https://www.tcl-lang.org/man/tcl8.6/TkCmd/frame.htm)|A rectangular region used as a container to organize complex layouts.|
|[LabelFrame](https://www.tcl-lang.org/man/tcl8.6/TkCmd/labelframe.htm)|A frame that includes a visible border and a title label.|
|[PanedWindow](https://www.tcl-lang.org/man/tcl8.6/TkCmd/panedwindow.htm)|A container that allows users to resize child panes by dragging a "sash."|
|[Toplevel](https://www.tcl-lang.org/man/tcl8.6/TkCmd/toplevel.htm)|A separate window that exists independently of the main application window.|
|[Canvas](https://www.tcl-lang.org/man/tcl8.6/TkCmd/canvas.htm)|A versatile area for drawing shapes, lines, images, or creating custom widgets.|

## Navigation & Selection Widgets
Used for managing multiple options or navigating the application.

|Element|Description|
|---|---|
|[Listbox](https://www.tcl-lang.org/man/tcl8.6/TkCmd/listbox.htm)|Displays a list of items from which a user can select one or more.|
|[Menu](https://www.tcl-lang.org/man/tcl8.6/TkCmd/menu.htm)|Used to create drop-down menus, context menus, and menu bars.|
|[Menubutton](https://www.tcl-lang.org/man/tcl8.6/TkCmd/menubutton.htm)|A button that opens a menu when clicked.|
|[Scrollbar](https://www.tcl-lang.org/man/tcl8.6/TkCmd/scrollbar.htm)|Provides scrolling capability for widgets like Canvas, Text, and Listbox.|

## Ttk (Themed Tk) Submodule
The tkinter.ttk module provides access to modern, themed versions of standard widgets and introduces several new ones:

|Element|Description|
|---|---|
|[Combobox](https://www.tcl-lang.org/man/tcl8.6/TkCmd/combobox.htm)|A combination of an Entry and a drop-down Listbox.|
|[Notebook](https://www.tcl-lang.org/man/tcl8.6/TkCmd/notebook.htm)|A tabbed container used to switch between different "pages" of a UI.|
|[Progressbar](https://www.tcl-lang.org/man/tcl8.6/TkCmd/progressbar.htm)|Visualizes the status of a long-running operation.|
|[Treeview](https://www.tcl-lang.org/man/tcl8.6/TkCmd/treeview.htm)|Displays data in a hierarchical (tree) or tabular (columns) format.|
|[Separator](https://www.tcl-lang.org/man/tcl8.6/TkCmd/separator.htm)|A simple horizontal or vertical line to visually divide sections.|
|[Sizegrip](https://www.tcl-lang.org/man/tcl8.6/TkCmd/sizegrip.htm)|A small handle at the bottom-right of a window to allow resizing.|

## Feedback & Dialogs
While not strictly "widgets" in the layout sense, these are built-in classes for standard UI interactions:

|Element|Description|
|---|---|
|[Messagebox](https://www.tcl-lang.org/man/tcl8.6/TkCmd/msgbox.htm)|Standardized pop-up alerts (info, warning, error, yes/no).|
|[FileDialog](https://www.tcl-lang.org/man/tcl8.6/TkCmd/filedialog.htm)|System-native windows for opening or saving files.|
|[ColorChooser](https://www.tcl-lang.org/man/tcl8.6/TkCmd/colorchooser.htm)|A standard interface for selecting colors.|