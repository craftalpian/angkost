import tkinter as tk
from tkinter import Label, ttk as ttk, Button, PhotoImage, Text, messagebox
from tkinter.font import Font
from turtle import home, title, update
from PIL import ImageTk, Image
import time

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        for F in (Home, Goods, Budget, Loading, Result):
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

        def logo_image(self):
            img_label = tk.Label(self, borderwidth=0)
            img_label.image = tk.PhotoImage(file="./assets/LogoSample_ByTailorBrands.jpg")
            img_label['image'] = img_label.image

            img_label.pack(pady=(38, 0))

        # Set background color white
        self.configure(background="white")

        # Home
        # logo_angkost = Image.open("./assets/LogoSample_ByTailorBrands.jpg")
        # resize_logo_angkost = logo_angkost.resize((210, 210), Image.ANTIALIAS)
        # tkinter_logo_angkost = ImageTk.PhotoImage(resize_logo_angkost)
        # logo_label = ttk.Label(
        #     self,
        #     image=tkinter_logo_angkost,
        #     padding=5,
        #     background="white"
        # )
        # logo_label.pack(pady=(38, 0))

        logo_image(self)

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

        def proccess():
            controller.show_frame(Budget)
            messagebox.showerror(title="Title", message="Test")

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
                              bg="white", command=proccess)
        login_button.pack(pady=(50, 0))


# Budget Screen
class Budget(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Set background color white
        self.configure(background="white")

        # Budget
        title = Label(self, text="Masukkan budget Anda:", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(120, 0))

        description = Label(self, text="Masukkan budget Anda untuk semua barang tersebut. Harap masukkan dalam rupiah ya!", font=Font(
            family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        input = Text(self, height=1, width=45, bg="#EDEDED", borderwidth=0,
                     fg="#625F5F", font=Font(family="Montserrat Regular", size=12))
        input.config(padx=16, pady=16)
        input.pack(pady=(30, 0))

        mulai_image = PhotoImage(file="./assets/mulai.png")
        login_button = Button(self, text='asnajksn', borderwidth=0,
                              bg="white", command=lambda: controller.show_frame(Result))
        login_button.pack(pady=(50, 0))

# Loading Screen
class Loading(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Set background color white
        self.configure(background="white")

        # Budget
        title = Label(self, text="Angkost sedang memproses...", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(250, 0))

        # lambda: controller.show_frame(Result)
        # self.after(5000, lambda: controller.show_frame(Result))

# Result Screen
class Result(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Set background color white
        self.configure(background="white")

        # Budget
        title = Label(self, text="Angkost menemukan hasil:", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(60, 0), padx=20, side= tk.TOP, anchor="w")

        description = Label(self, text="Masukkan budget Anda untuk semua barang tersebut. Harap masukkan dalam rupiah ya!", font=Font(
            family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        input = Text(self, height=1, width=45, bg="#EDEDED", borderwidth=0,
                     fg="#625F5F", font=Font(family="Montserrat Regular", size=12))
        input.config(padx=16, pady=16)
        input.pack(pady=(30, 0))

        mulai_image = PhotoImage(file="./assets/mulai.png")
        login_button = Button(self, text='asnajksn', borderwidth=0,
                              bg="white", command=lambda: controller.show_frame(Loading))
        login_button.pack(pady=(50, 0))

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
