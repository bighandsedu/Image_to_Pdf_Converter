from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os


def open_files():
    _images = []
    _names = list(tk.filedialog.askopenfilenames(initialdir=os.getcwd(), title="Open Files / Select Images",
                                                filetypes=[("PNG Files", ".png"), ("JPG Files", ".jpg"),
                                                           ("All Files", ".*")]))

    for name in _names:
        _image = Image.open(name)
        _images.append(_image)

    return _images


def convert_save(_images):
    _converted_images = []
    for image in _images:
        image_converted = image.convert("RGB")
        _converted_images.append(image_converted)

    convert_image_copy = _converted_images.copy()
    convert_image_copy.pop(0)

    save_as = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save Files",
                                           filetypes=[("PDF File",".pdf")], defaultextension= ".pdf")

    _converted_images[0].save(save_as, save_all=True, append_images=convert_image_copy)


images = open_files()
convert_save(images)