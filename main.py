__author__ = "Hummingbird Studio™"
__copyright__ = "Copyright (C) 2023 Lolkai"
__version__ = "1.0"

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
 
root = Tk()
root.geometry("240x64")
root.title("img-rar")
if os.path.isfile("icon.ico"):
    root.iconbitmap("icon.ico")

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=0)
root.grid_columnconfigure(index=2, weight=1)
value = 1
# открываем файл в текстовое поле
def open_rar():
    global rar
    filepath = filedialog.askopenfilename(filetypes=[("RAR files", '*.rar'),
        ("ZIP files", '*.zip'), ("7z files", '*.7z'), ("ARJ files", '*.arj'), 
        ("CAB files", '*.cab'), ("TAR files", '*.tar'), ("LZH files", '*.lzh'),
        ("LZ files", '*.lz'), ("GZip files", '*.gzip'), ("TAR files", '*.tar'), 
        ("UUE files", '*.uue'), ("ISO files", '*.iso'), ("BZIP2 files", '*.BZIP2'), 
        ("BZIP2 files", '*.bzip2'), ("XZ files", '*.xz'), ("Z files", '*.z'), 
        ("BZ2 files", '*.bz2'), ("GZ files", '*.gz'), 
        ("ZIPX files", '*.zipx'), ("ZST files", '*.zst'), 
        ("001 files", '*.001'), ("All files", "*")], title="Choose file name", defaultextension="rar")
    if filepath != "":
        with open(filepath, "r") as file:
            rar = filepath
            rar = rar.replace('/', '\\')
            print(rar)

def open_img():
    global img
    filepath = filedialog.askopenfilename(filetypes=[("JPG files", '*.jpg'), 
        ("PNG files", '*.png'), ("GIF files", '*.gif'),("TIFF files", '*.tiff'), 
        ("BMP files", '*.bmp'), ("SVG files (File error)", '*.svg'), 
        ("WEBP files", '*.webp'), ("AI files", '*.ai'), ("CDR files", '*.cdr'), 
        ("HEIF files", '*.heif'), ("AVIF files", '*.avif'), ("ICO files", '*.ico'), 
        ("ICNS files", '*.icns'), ("All files", "*")], title="Choose file name", defaultextension="jpg")
    if filepath != "":
        with open(filepath, "r") as file:
            img = filepath
            img = img.replace('/', '\\')
            print(img)
 
# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename(initialfile='output.jpg', 
        filetypes=[("JPG files", '*.jpg'), ("PNG files", '*.png'), 
        ("GIF files", '*.gif'), ("TIFF files", '*.tiff'), ("BMP files", '*.bmp'), 
        ("PSD files", '*.psd'), ("SVG files (File error)", '*.svg'), 
        ("WEBP files", '*.webp'), ("AI files", '*.ai'), ("CDR files", '*.cdr'), 
        ("HEIF files", '*.heif'), ("AVIF files", '*.avif'), ("ICO files", '*.ico'), 
        ("ICNS files", '*.icns'), ("All files", "*"),], title="Choose file name", defaultextension="jpg")
    if filepath != "":
        with open(filepath, "w") as file:
            output = filepath
            output = output.replace('/', '\\')
            img.encode()
            rar.encode()
            output.encode()
    os.system(f"type {img} {rar} > {output}")

PADX = 3
open_button = ttk.Button(text="Open rar", command=open_rar)
open_button.grid(column=0, row=1, sticky=NSEW, padx=PADX)

open_button = ttk.Button(text="Open img", command=open_img)
open_button.grid(column=1, row=1, sticky=NSEW, padx=PADX)
 
save_button = ttk.Button(text="Save file", command=save_file)
save_button.grid(column=2, row=1, sticky=NSEW, padx=PADX)

frame = Frame(root)
frame.grid(column=1, row=2, sticky="w", padx=0)

def other():
    global value
    value *= -1
    if value < 0:
        label = Label(frame, text="Hummingbird Studio\nCopyright © Lolkai").grid()
    else:
        for widgets in frame.winfo_children():
            widgets.grid_forget()
        open_button.grid(column=0, row=1, sticky=NSEW, padx=PADX)
        open_button.grid(column=1, row=1, sticky=NSEW, padx=18)
        save_button.grid(column=2, row=1, sticky=NSEW, padx=PADX)

Btn1 = Button(root, text="►", command=other)
Btn1.grid(row=2, sticky="w", pady=6)

root.attributes("-topmost", 'True')
root.resizable(False, False)
root.mainloop()