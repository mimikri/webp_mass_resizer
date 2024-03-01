import os
from tkinter import *
from tkinter import filedialog
from PIL import Image


def resize_webp_files():
    folder_path = folder_path_var.get()
    dest_folder_path = dest_folder_path_var.get()
    append_text = append_var.get()
    max_width = int(max_width_var.get()) if max_width_var.get() else None
    resize_percentage = int(resize_percentage_var.get()) if resize_percentage_var.get() else None
    quality = int(quality_var.get()) if quality_var.get() else None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                file_path = os.path.join(root, file)
                image = Image.open(file_path)
                width, height = image.size
                if max_width and width > max_width:
                    new_width = max_width
                    new_height = int(height * (max_width / width))
                    image = Image.open(file_path)
                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                if resize_percentage:
                    new_width = int(width * (resize_percentage / 100))
                    new_height = int(height * (resize_percentage / 100))
                    image = Image.open(file_path)
                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                if quality:
                    image.save(os.path.join(dest_folder_path, f"{os.path.splitext(file)[0]}{append_text}.webp"), quality=quality)
                else:
                    image.save(os.path.join(dest_folder_path, f"{os.path.splitext(file)[0]}{append_text}.webp"))


# Create GUI
root = Tk()
root.title("WebP Resizer")

folder_path_var = StringVar()
dest_folder_path_var = StringVar()
append_var = StringVar()
max_width_var = StringVar()
resize_percentage_var = StringVar()
quality_var = StringVar()
folder_path_var.set(os.getcwd())
dest_folder_path_var.set(os.getcwd())
append_var.set("_50")
resize_percentage_var.set(50)
quality_var.set(90)

Label(root, text="Source Folder Path:").grid(row=0, column=0)
# Set the value of the folder_path_var using the set method

Entry(root, textvariable=folder_path_var).grid(row=0, column=1, sticky="ew")
Button(root, text="Browse", command=lambda: folder_path_var.set(filedialog.askdirectory())).grid(row=0, column=2)

Label(root, text="Destination Folder Path:").grid(row=1, column=0)
Entry(root, textvariable=dest_folder_path_var).grid(row=1, column=1)
Button(root, text="Browse", command=lambda: dest_folder_path_var.set(filedialog.askdirectory())).grid(row=1, column=2)

Label(root, text="Append Text:").grid(row=2, column=0)
Entry(root, textvariable=append_var).grid(row=2, column=1)

Label(root, text="Max Width (optional):").grid(row=3, column=0)
Entry(root, textvariable=max_width_var).grid(row=3, column=1)

Label(root, text="Resize Percentage (optional):").grid(row=4, column=0)
Entry(root, textvariable=resize_percentage_var).grid(row=4, column=1)

Label(root, text="Quality (optional):").grid(row=5, column=0)
Entry(root, textvariable=quality_var).grid(row=5, column=1)

Button(root, text="Resize WebP Files", command=resize_webp_files).grid(row=6, column=1)
# Set the column width as a percentage of the window width
root.columnconfigure(1, weight=1)  # Set the width of column 1 to expand with the window

Entry(root, textvariable=folder_path_var).grid(row=0, column=1, sticky="ew", ipadx=200)
Entry(root, textvariable=dest_folder_path_var).grid(row=1, column=1, sticky="ew")
Entry(root, textvariable=append_var).grid(row=2, column=1, sticky="ew")
Entry(root, textvariable=max_width_var).grid(row=3, column=1, sticky="ew")
Entry(root, textvariable=resize_percentage_var).grid(row=4, column=1, sticky="ew")
Entry(root, textvariable=quality_var).grid(row=5, column=1, sticky="ew")
root.mainloop()