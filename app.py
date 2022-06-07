import tkinter as tk
from tkinter import Label, ttk as ttk, Button, PhotoImage, messagebox
from tkinter.font import Font
from turtle import home, title, update
from PIL import ImageTk, Image

root = tk.Tk(screenName="Angkost")
root.title("Angkost")
root.geometry("680x600")
root.resizable(False, False)
root.iconbitmap("./assets/angkost-icon.ico")
root.configure(background="white")

screen = "home"

frame = ttk.Frame(root)

def update_screen():
    global screen
    screen = "goods"

if screen == "home":
    # Home
    logo_angkost = Image.open("./assets/LogoSample_ByTailorBrands.jpg")
    resize_logo_angkost = logo_angkost.resize((210, 210), Image.ANTIALIAS)
    tkinter_logo_angkost = ImageTk.PhotoImage(resize_logo_angkost)
    logo_label = ttk.Label(
        root,
        image=tkinter_logo_angkost,
        padding=5,
        background="white"
    )
    logo_label.pack(pady=(38, 0))

    title = Label(root, text="Halo, selamat datang di Angkost", font=Font(
                family="Montserrat Medium", size=22, weight="normal"), background="white")
    title.pack(pady=(16, 0))

    description = Label(root, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.", font=Font(family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
    description.pack(pady=(16, 0), padx=52)

    mulai_image = PhotoImage(file="./assets/mulai.png")
    login_button = Button(root, image=mulai_image, borderwidth=0, bg="white", command=update_screen)
    login_button.pack(pady=(50, 0))

root.mainloop()
