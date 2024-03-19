from convert_path import convert_path, current_os
import tkinter as tk
from tkinter import Entry, Button, Text, font as tkfont, Radiobutton, IntVar, StringVar, Label
import os
import webbrowser  # Import the webbrowser module for opening the folder in the file explorer

# Event handler for the platform radio buttons
def platform_selection_changed():
    convert_button_clicked()

# Event handler for the "Convert" button
def convert_button_clicked(*args):
    input_text = input_entry.get().strip()  # Remove quotes from the input
    # Remove single and double quotes from the input
    input_text = input_text.replace("'", "").replace('"', '')
    to_platform = platform_var.get()  # Get the selected platform
    converted_text = convert_path(input_text, "w" if to_platform == 0 else "l")
    output_text.delete(1.0, tk.END)  # Clear previous content
    output_text.insert(tk.END, converted_text)
    update_path_info()
    update_copy_button_state()  # Check and update the "Copy" button state


# Event handler for the "Copy" button
def copy_button_clicked():
    converted_text = output_text.get(1.0, tk.END).strip()
    app.clipboard_clear()
    app.clipboard_append(converted_text)
    app.update()
    update_copy_button_state()  # Check and update the button state

# Update the "Copy" button's state
def update_copy_button_state():
    if output_text.get(1.0, tk.END).strip():  # Check if there is text to be copied
        copy_button["state"] = "active"  # Enable the button
    else:
        copy_button["state"] = "disabled"  # Disable the button

# "Open folder" button clicked
def open_folder_button_clicked():
    converted_path = output_text.get(1.0, tk.END).strip()
    converted_path = convert_path(converted_path, current_os)

    if os.path.isfile(converted_path):
        folder_path = os.path.dirname(converted_path)
        webbrowser.open(folder_path)
    elif os.path.isdir(converted_path):
        webbrowser.open(converted_path)

# Execute the conversion when Enter key is pressed
def handle_enter(event):
    convert_button_clicked()

# Update the path information
def update_path_info():
    converted_path = output_text.get(1.0, tk.END).strip()
    converted_path = convert_path(converted_path, current_os)

    if os.path.isfile(converted_path):
        path_info.set("This input/output path is a known file. Click 'Open folder' to open its directory.")
        open_folder_button["state"] = "active"  # Enable the button
    elif os.path.isdir(converted_path):
        path_info.set("This input/output path is a known folder. Click 'Open folder' to open it.")
        open_folder_button["state"] = "active"  # Enable the button
    else:
        path_info.set("This input/output path is not a known file or folder.")
        open_folder_button["state"] = "disabled"  # Disable the "Open folder" button

# Create the main application window
app = tk.Tk()
app.title("Path Converter App")

# Set the font for all widgets to the default font
default_font = tkfont.nametofont("TkDefaultFont")

# Input Entry
input_label = tk.Label(app, text="Input path:", font=default_font)
input_label.grid(row=0, column=0, columnspan=3)  # Add padding
input_entry = Entry(app, width=100, font=default_font)  # Set the width and font
input_entry.grid(row=1, column=0, columnspan=3)  # Add padding

# Radiobuttons for platform selection
platform_var = IntVar()
windows_button = Radiobutton(app, text="To Windows Path", variable=platform_var, value=0, font=default_font, command=platform_selection_changed)
linux_button = Radiobutton(app, text="To Unix/Linux/Mac Path", variable=platform_var, value=1, font=default_font, command=platform_selection_changed)
windows_button.grid(row=2, column=0)
linux_button.grid(row=2, column=1)

# Default to the current OS
if current_os == "w":
    platform_var.set(0)
    windows_button.select()
else:
    platform_var.set(1)
    linux_button.select()

# Convert Button
convert_button = Button(app, text="Convert", command=convert_button_clicked, font=default_font)  # Set the font
convert_button.grid(row=4, column=0, columnspan=3, pady=20)  # Centered and spanning 3 columns

# Output Text (Selectable)
output_text = Text(app, height=1, width=100, font=default_font)  # Set the width and font
output_text.grid(row=6, column=0, columnspan=3)  # Centered and spanning 3 columns

# "Copy" Button
copy_button = Button(app, text="Copy", command=copy_button_clicked, font=default_font, state="disabled")  # Set the font
copy_button.grid(row=7, column=0, pady=5, sticky="e", padx=5)  # Right-aligned

# "Open folder" Button (Initially disabled)
open_folder_button = Button(app, text="Open folder", command=open_folder_button_clicked, font=default_font, state="disabled")  # Set the font and state
open_folder_button.grid(row=7, column=1, pady=5, sticky="w", padx=5)  # Left-aligned

# Label to display path information
path_info = StringVar()
path_info_label = Label(app, textvariable=path_info, font=default_font)
path_info_label.grid(row=8, column=0, columnspan=2, pady=5)

# Configure grid column weights to make the input and output fields expand
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Bind the Enter key to execute the conversion
app.bind('<Return>', handle_enter)

# Start the main event loop
app.mainloop()
