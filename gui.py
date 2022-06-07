import tkinter as tk
from tkinter import Label, ttk as ttk, Button, PhotoImage
from tkinter.font import Font
from turtle import home, title
from PIL import ImageTk, Image

class AngkostGUI:
    def __init__(self):
        # Set screen name to Angkost
        self.root = tk.Tk(screenName="Angkost")
        # Set screen title to Angkost
        self.root.title("Angkost")
        # Set screen dimension 680x600
        self.root.geometry("680x600")
        # Set disable screen resize
        self.root.resizable(False, False)
        # Set screen icon
        self.root.iconbitmap("./assets/angkost-icon.ico")
        # Set screen background color to white
        self.root.configure(background="white")

        self.frame = ttk.Frame(self.root)

    def home(self):
        # Logo
        logo_angkost = Image.open("./assets/LogoSample_ByTailorBrands.jpg")
        resize_logo_angkost = logo_angkost.resize((210, 210), Image.ANTIALIAS)
        tkinter_logo_angkost = ImageTk.PhotoImage(resize_logo_angkost)
        logo_label = ttk.Label(
            self.root,
            image=tkinter_logo_angkost,
            padding=5,
            background="white"
        )
        logo_label.pack(pady=(38, 0))

        # Title
        title = Label(self.root, text="Halo, selamat datang di Angkost", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(16, 0))

        # Description
        description = Label(self.root, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.", font=Font(family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        # "Mulai" button
        mulai_image = PhotoImage(file="./assets/mulai.png")
        login_button = Button(self.root, image=mulai_image, borderwidth=1, bg="white")
        login_button.pack(pady=(50, 0))

    def start(self):
        self.home()
        # self.root.mainloop()
