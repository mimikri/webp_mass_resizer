import os
from tkinter import *
from tkinter import filedialog
from PIL import Image


import os
from PIL import Image

def resize_webp_files(folder_path_var, dest_folder_path_var, append_var, max_width_var, fixed_width_var, fixed_height_var, quality_var, resize_percentage_var):
    folder_path = folder_path_var.get()
    dest_folder_path = dest_folder_path_var.get()
    append_text = append_var.get()
    max_width = int(max_width_var.get()) if max_width_var.get() else None
    fixed_width = int(fixed_width_var.get()) if fixed_width_var.get() else None
    fixed_height = int(fixed_height_var.get()) if fixed_height_var.get() else None
    quality = int(quality_var.get()) if quality_var.get() else None
    resize_percentage = int(resize_percentage_var.get()) if resize_percentage_var.get() else None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".webp"):
                file_path = os.path.join(root, file)
                image = Image.open(file_path)
                width, height = image.size

                # Apply fixed width and height if provided
                if fixed_width and fixed_height:
                    new_width = fixed_width
                    new_height = fixed_height
                elif fixed_width:
                    new_width = fixed_width
                    new_height = int(height * (fixed_width / width))
                elif fixed_height:
                    new_height = fixed_height
                    new_width = int(width * (fixed_height / height))
                else:
                    # Apply max width if provided and it dominates the dimensions
                    if resize_percentage:
                        new_width = int(width * (resize_percentage / 100))
                        new_height = int(height * (resize_percentage / 100))
                    else:
                        new_width = width
                        new_height = height
                    if max_width and new_width > max_width:
                        new_width = max_width
                        new_height = int(height * (max_width / width))

                image = image.resize((new_width, new_height), Image.LANCZOS)
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
fixed_width_var = StringVar()
fixed_height_var = StringVar()
fixed_width_var.set("")
fixed_height_var.set("")
Label(root, text="Source Folder Path:").grid(row=0, column=0, sticky=E)
Button(root, text="Browse", command=lambda: folder_path_var.set(filedialog.askdirectory())).grid(row=0, column=2)
Label(root, text="Destination Folder Path:").grid(row=1, column=0, sticky=E)
Button(root, text="Browse", command=lambda: dest_folder_path_var.set(filedialog.askdirectory())).grid(row=1, column=2)
Label(root, text="Append to filename:").grid(row=2, column=0, sticky=E)
Label(root, text="Quality:").grid(row=4, column=0, sticky=E)
Label(root, text="").grid(row=5, column=0, sticky=E)
Label(root, text="Resize with percentage", font=("Arial", 12, "bold")).grid(row=6, column=1, columnspan=2, sticky=W)
Label(root, text="Resize Percentage:").grid(row=7, column=0, sticky=E)
Label(root, text="Max Width (optional):").grid(row=8, column=0, sticky=E)
Label(root, text="").grid(row=9, column=0, sticky=E)
Label(root, text="Resize with fixed pixels (optional)", font=("Arial", 12, "bold")).grid(row=10, column=1,columnspan=2, sticky=W)
Label(root, text="Fixed Width:").grid(row=11, column=0, sticky=E)
Label(root, text="Fixed Height:").grid(row=12, column=0, sticky=E)


Button(root, text="Resize WebP Files", command=lambda: resize_webp_files(folder_path_var, dest_folder_path_var, append_var, max_width_var, fixed_width_var, fixed_height_var, quality_var, resize_percentage_var)).grid(row=13, column=1)
# Set the column width as a percentage of the window width
root.columnconfigure(1, weight=1)  # Set the width of column 1 to expand with the window

Entry(root, textvariable=folder_path_var).grid(row=0, column=1, sticky="ew", ipadx=150)
Entry(root, textvariable=dest_folder_path_var).grid(row=1, column=1, sticky="ew")
Entry(root, textvariable=append_var).grid(row=2, column=1, sticky="ew")
Entry(root, textvariable=quality_var).grid(row=4, column=1, sticky="ew")
Entry(root, textvariable=resize_percentage_var).grid(row=7, column=1, sticky="ew")
Entry(root, textvariable=max_width_var).grid(row=8, column=1, sticky="ew")

Entry(root, textvariable=fixed_width_var).grid(row=11, column=1, sticky="ew")
Entry(root, textvariable=fixed_height_var).grid(row=12, column=1, sticky="ew")
root.mainloop()