import tkinter as tk
from tkinter import Label, ttk as ttk, Button, Text, messagebox
from tkinter.font import Font
from tokopedia import get_product_info
from data import extract_data, final_result
from cProfile import label
from PIL import ImageTk
from urllib.request import urlopen

budget, goods, goods_result, result_data = 0, [], [], []

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        for F in (Home, Goods, Budget, Result):
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

        # Logo Angkost
        def logo_image(self):
            img_label = tk.Label(self, borderwidth=0)
            img_label.image = tk.PhotoImage(
                file="./assets/LogoSample_ByTailorBrands.jpg")
            img_label['image'] = img_label.image

            img_label.pack(pady=(38, 0))

        # Set background color white
        self.configure(background="white")

        # Home
        logo_image(self)

        # Title of app
        title = Label(self, text="Halo, selamat datang di Angkost", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(16, 0))

        # Description of app
        description = Label(self, text="Angkost akan membantu Anda dalam mencari barang kebutuhan di kost. Silakan tekan tombol di bawah ini untuk melanjutkan.", font=Font(
            family="Montserrat Medium", size=12), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(16, 0), padx=52)

        # Start button
        start_button = Button(self, text="Mulai", borderwidth=0,
                              bg="#525252", fg="white", command=lambda: controller.show_frame(Result), width=16, height=1, font=Font(
                                  family="Montserrat Bold", size=12, weight="normal"))
        start_button.pack(pady=(60, 0))

# Goods Page


class Goods(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        def proccess():
            goods_input = input.get("1.0", "end-1c")

            if len(goods_input) < 1:
                messagebox.showerror(
                    title="Bermasalah!", message="Harap masukkan daftar barang yang Anda inginkan dengan benar!")
            elif goods_input.count(",") > 4:
                messagebox.showerror(
                    title="Bermasalah!", message="Harap masukkan daftar barang tidak lebih dari 5!")
            else:
                for i in goods_input.split(","):
                    goods.append(i.strip())
                    goods_result.append(extract_data(get_product_info(i.strip())[
                                        0]['data']['ace_search_product_v4']['data']['products']))

                messagebox.showinfo(
                    title="Angkost", message="Berhasil melakukan pengambilan data...")

                controller.show_frame(Budget)

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

        # Next button
        next_button = Button(self, text="Selanjutnya", borderwidth=0,
                             bg="#525252", fg="white", command=proccess, width=16, height=1, font=Font(
                                 family="Montserrat Bold", size=12, weight="normal"))
        next_button.pack(pady=(60, 0))

# Budget Screen


class Budget(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def proccess():
            budget_input = input.get("1.0", "end-1c")

            if len(budget_input) < 1:
                messagebox.showerror(
                    title="Bermasalah!", message="Harap masukkan harga dengan benar!")
            else:
                try:
                    if int(budget_input) <= 1:
                        messagebox.showwarning(
                            title="Bermasalah!", message="Masukkan budget minimal 1 rupiah")
                    else:
                        global budget, result_data
                        budget = int(budget_input)

                        result_data = final_result(goods, goods_result, budget)

                        controller.show_frame(Result)
                except Exception as e:
                    print(e)
                    messagebox.showwarning(
                        title="Bermasalah!", message="Masukkan budget dengan angka!")

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

        # Next button
        next_button = Button(self, text="Selanjutnya", borderwidth=0,
                             bg="#525252", fg="white", command=proccess, width=16, height=1, font=Font(
                                 family="Montserrat Bold", size=12, weight="normal"))
        next_button.pack(pady=(60, 0))

# Result Screen


class Result(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set background color white
        self.configure(background="white")

        # Budget
        title = Label(self, text="Angkost menemukan hasil:", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(60, 0), padx=20, side=tk.TOP, anchor="w")

        description = Label(self, text="Daftar yang ditampilkan adalah barang termurah", font=Font(
            family="Montserrat Medium", size=10), background="white", wraplength=540, justify="center", fg="#4F4F4F")
        description.pack(pady=(4, 0), padx=20, side=tk.TOP, anchor="w")

        # IMAGE
        imageUrl = "https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-Sticky-EW.png"
        u = urlopen(imageUrl)
        raw_data = u.read()
        u.close()

        photo = ImageTk.PhotoImage(data=raw_data)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.config(height=40, width=40)
        label.pack(pady=(4, 0), padx=20, side=tk.TOP, anchor="w")

        product_title = Label(self, text="Bangku Belajar Ikea", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white")
        product_title.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        price_title = Label(self, text="Rp350.000", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        price_title.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        # l = Button(self, text="Left")
        # l.place(x=50, y=50)
        # m = Button(self, text="Middle")
        # m.place(x=70, y=50)

        login_button = Button(self, text='asnajksn', borderwidth=0,
                              bg="white", command=lambda: controller.show_frame(Home))
        login_button.pack(pady=(50, 0))


# Driver Code
app = tkinterApp()

# Styling app
app.title("Angkost")
app.geometry("680x600")
app.resizable(False, True)
app.iconbitmap("./assets/angkost-icon.ico")
app.configure(background="white")

# Loop app
app.mainloop()
