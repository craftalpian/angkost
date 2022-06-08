import tkinter as tk
from tkinter import Label, ttk as ttk, Button, PhotoImage, Text
from tkinter.font import Font
from turtle import home, title, update
from PIL import ImageTk, Image

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        for F in (Home, Goods, Page2):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Home Page


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set background color white
        self.configure(background="white")

        # Home
        logo_angkost = Image.open("./assets/LogoSample_ByTailorBrands.jpg")
        resize_logo_angkost = logo_angkost.resize((210, 210), Image.ANTIALIAS)
        tkinter_logo_angkost = ImageTk.PhotoImage(resize_logo_angkost)
        logo_label = ttk.Label(
            self,
            image=tkinter_logo_angkost,
            padding=5,
            background="white"
        )
        logo_label.pack(pady=(38, 0))

        title = Label(self, text="Halo, selamat datang di Angkost", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(16, 0))

        description = Label(self, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.", font=Font(
            family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        mulai_image = PhotoImage(file="./assets/mulai.png")
        login_button = Button(self, text='asnajksn', borderwidth=0,
                              bg="white", command=lambda: controller.show_frame(Goods))
        login_button.pack(pady=(50, 0))

# Goods Page


class Goods(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # Set background color white
        self.configure(background="white")

        # Goods
        title = Label(self, text="Masukkan daftar barang:", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(120, 0))

        description = Label(self, text="Anda dapat memasukkan lebih dari 1 barang dengan menggunakan , (koma) sebagai pemisah. Maksimal 5 barang.", font=Font(
            family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        input = Text(self, height=5, width=45, bg="#EDEDED", borderwidth=0,
                     fg="#625F5F", font=Font(family="Montserrat Regular", size=12))
        input.config(padx=16, pady=16)
        input.pack(pady=(30, 0))

        mulai_image = PhotoImage(file="./assets/mulai.png")
        login_button = Button(self, text='asnajksn', borderwidth=0,
                              bg="white", command=lambda: controller.show_frame(Goods))
        login_button.pack(pady=(50, 0))


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Goods))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(Home))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()

# Styling app
app.title("Angkost")
app.geometry("680x600")
app.resizable(False, False)
app.iconbitmap("./assets/angkost-icon.ico")
app.configure(background="white")

# Loop app
app.mainloop()
