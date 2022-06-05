import requests as rs
import numpy as np
import tkinter as tk
from tkinter import Label, ttk as ttk
from tkinter.font import Font
from PIL import ImageTk, Image

root = tk.Tk(screenName="Angkost")
root.title("Angkost")
root.geometry("680x600")
root.resizable(False, False)
root.iconbitmap("./assets/angkost-icon.ico")
root.configure(background="white")

frm = ttk.Frame(root)
image = Image.open("./assets/LogoSample_ByTailorBrands.jpg")
image = image.resize((210, 210), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(
    root,
    image=photo,
    padding=5,
    background="white"
)
image_label.pack(pady=(58, 0))

judul = Label(root, text="Halo, selamat datang di Angkost",
              font=Font(family="Montserrat", size=16, weight="normal"), background="white")
judul.pack(pady=(16, 0))
deskripsi = Label(root, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.",
              font=Font(family="Montserrat", size=12), background="white", wraplength=600, justify="center", fg="#4F4F4F")
deskripsi.pack(pady=(16, 0), padx=52)
root.mainloop()
