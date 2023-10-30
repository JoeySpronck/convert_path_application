from convert_path import convert_path, current_os
import tkinter as tk
from tkinter import Entry, Button, Text, font as tkfont, Radiobutton, IntVar, StringVar, Label
import os

# Event handler for the platform radio buttons
def platform_selection_changed():
    convert_button_clicked()

# Event handler for the "Convert" button
def convert_button_clicked(*args):
    input_text = input_entry.get()
    to_platform = platform_var.get()  # Get the selected platform
    converted_text = convert_path(input_text, "w" if to_platform == 0 else "l")
    output_text.delete(1.0, tk.END)  # Clear previous content
    output_text.insert(tk.END, converted_text)
    update_path_type()

# Event handler for the "Copy" button
def copy_button_clicked():
    converted_text = output_text.get(1.0, tk.END).strip()
    app.clipboard_clear()
    app.clipboard_append(converted_text)
    app.update()

# Execute the conversion when Enter key is pressed
def handle_enter(event):
    convert_button_clicked()

# Update the path type label
def update_path_type():
    converted_path = output_text.get(1.0, tk.END).strip()

    if os.path.isfile(convert_path(converted_path, current_os)):
        path_type.set("This input/output path is a file.")
    elif os.path.isdir(convert_path(converted_path, current_os)):
        path_type.set("This input/output path is a folder.")
    else:
        path_type.set("This input/output path is not a file or folder that is currently available to your system.")

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
convert_button.grid(row=4, column=0, columnspan=3, pady=10)  # Centered and spanning 3 columns

# "Converted path:" Label
converted_label = tk.Label(app, text="Converted path:", font=default_font)
converted_label.grid(row=5, column=0, columnspan=3)  # Centered and spanning 3 columns

# Output Text (Selectable)
output_text = Text(app, height=1, width=100, font=default_font)  # Set the width and font
output_text.grid(row=6, column=0, columnspan=3)  # Centered and spanning 3 columns

# Copy Button
copy_button = Button(app, text="Copy", command=copy_button_clicked, font=default_font)  # Set the font
copy_button.grid(row=7, column=0, columnspan=3)  # Centered and spanning 3 columns

# Label to display path type information
path_type = StringVar()
path_type_label = Label(app, textvariable=path_type, font=default_font)
path_type_label.grid(row=8, column=0, columnspan=3)

# Configure grid column weights to make the input and output fields expand
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Bind the Enter key to execute the conversion
app.bind('<Return>', handle_enter)

# Start the main event loop
app.mainloop()
