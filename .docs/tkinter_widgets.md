# tkinter Widgets
Quick reference cheat sheet of tkinter widgets.
Links should all work but some may not be correct yet. Primary links point to Python-focused `tkdocs.com`, while `[TclDoc]` links point to the main Tcl/Tk reference.

## Input & Display Widgets

These are the foundational components used to interact with or show data.

|Element|Description|
|---|---|
|[Label](https://tkdocs.com/shipman/label.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/label.htm))|Displays text or images. It is non-interactive.|
|[Button](https://tkdocs.com/shipman/button.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/button.htm))|A standard clickable button to trigger actions.|
|[Entry](https://tkdocs.com/shipman/entry.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm))|A single-line text field for user input.|
|[Text](https://tkdocs.com/shipman/text.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/text.htm))|A multi-line text area allowing for complex formatting and editing.|
|[Checkbutton](https://tkdocs.com/shipman/checkbutton.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/checkbutton.htm))|A toggle switch representing a boolean state (on/off).|
|[Radiobutton](https://tkdocs.com/shipman/radiobutton.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/radiobutton.htm))|Used to select one option from a predefined set.|
|[Scale](https://tkdocs.com/shipman/scale.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/scale.htm))|A slider bar for selecting a numeric value from a range.|
|[Spinbox](https://tkdocs.com/shipman/spinbox.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/spinbox.htm))| An entry field with "up" and "down" arrows to increment/decrement values.|

## Container & Layout Widgets
These widgets organize and group other elements within the UI.

|Element|Description|
|---|---|
|[Frame](https://tkdocs.com/shipman/frame.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/frame.htm))|A rectangular region used as a container to organize complex layouts.|
|[LabelFrame](https://tkdocs.com/shipman/labelframe.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/labelframe.htm))|A frame that includes a visible border and a title label.|
|[PanedWindow](https://tkdocs.com/shipman/panedwindow.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/panedwindow.htm))|A container that allows users to resize child panes by dragging a "sash."|
|[Toplevel](https://tkdocs.com/shipman/toplevel.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/toplevel.htm))|A separate window that exists independently of the main application window.|
|[Canvas](https://tkdocs.com/shipman/canvas.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/canvas.htm))|A versatile area for drawing shapes, lines, images, or creating custom widgets.|

## Navigation & Selection Widgets
Used for managing multiple options or navigating the application.

|Element|Description|
|---|---|
|[Listbox](https://tkdocs.com/shipman/listbox.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/listbox.htm))|Displays a list of items from which a user can select one or more.|
|[Menu](https://tkdocs.com/shipman/menu.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/menu.htm))|Used to create drop-down menus, context menus, and menu bars.|
|[Menubutton](https://tkdocs.com/shipman/menubutton.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/menubutton.htm))|A button that opens a menu when clicked.|
|[Scrollbar](https://tkdocs.com/shipman/scrollbar.html)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/scrollbar.htm))|Provides scrolling capability for widgets like Canvas, Text, and Listbox.|

## Ttk (Themed Tk) Submodule
The tkinter.ttk module provides access to modern, themed versions of standard widgets and introduces several new ones:

|Element|Description|
|---|---|
|[Combobox](https://tkdocs.com/shipman/ttk-Combobox.html)|A combination of an Entry and a drop-down Listbox.|
|[Notebook](https://tkdocs.com/shipman/ttk-Notebook.html)|A tabbed container used to switch between different "pages" of a UI.|
|[Progressbar](https://tkdocs.com/shipman/ttk-Progressbar.html)|Visualizes the status of a long-running operation.|
|[Treeview](https://tkdocs.com/shipman/ttk-Treeview.html)|Displays data in a hierarchical (tree) or tabular (columns) format.|
|[Separator](https://tkdocs.com/shipman/ttk-Separator.html)|A simple horizontal or vertical line to visually divide sections.|
|[Sizegrip](https://tkdocs.com/shipman/ttk-Sizegrip.html)|A small handle at the bottom-right of a window to allow resizing.|

## Feedback & Dialogs
While not strictly "widgets" in the layout sense, these are built-in classes for standard UI interactions:

|Element|Description|
|---|---|
|[Messagebox](https://tkdocs.com/shipman/msgbox.htm)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/msgbox.htm))|Standardized pop-up alerts (info, warning, error, yes/no).|
|[FileDialog](https://tkdocs.com/shipman/filedialog.htm)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/filedialog.htm))|System-native windows for opening or saving files.|
|[ColorChooser](https://tkdocs.com/shipman/colorchooser.htm)([TclDoc](https://www.tcl-lang.org/man/tcl8.6/TkCmd/colorchooser.htm))|A standard interface for selecting colors.|