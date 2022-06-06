import requests as rs
import numpy as np
import tkinter as tk
from tkinter import Label, ttk as ttk, Button, PhotoImage
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
image_label.pack(pady=(38, 0))

judul = Label(root, text="Halo, selamat datang di Angkost",
              font=Font(family="Montserrat Medium", size=22, weight="normal"), background="white")
judul.pack(pady=(16, 0))

deskripsi = Label(root, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.",
                  font=Font(family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
deskripsi.pack(pady=(16, 0), padx=52)


def selanjutnya(e):
    print("ditekan")

loginImg = PhotoImage(file="./assets/mulai.png")

loginBtn = Button(root, image=loginImg, command=selanjutnya("a"), borderwidth=0)
# button1 = Button(root, text="Mulai", command=selanjutnya(
#     'test'), font=Font(family="Montserrat Bold", size=12), bg="#525252", fg="white", width=15, height=1, borderwidth=1)
# button1.config(height=28,
# 			  width=113)
# put on screen
# pady=(16, 0), padx=52
loginBtn.pack(pady=(50, 0))

root.mainloop()
