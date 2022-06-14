import tkinter as tk
from tkinter import Label, ttk as ttk, Button, Text, messagebox
from tkinter.font import Font
from tokopedia import get_product_info
from data import extract_data, final_result, short, thousand_format, clear
import webbrowser

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
                              bg="#525252", fg="white", command=lambda: controller.show_frame(Goods), width=16, height=1, font=Font(
                                  family="Montserrat Bold", size=12, weight="normal"))
        start_button.pack(pady=(60, 0))

# Goods Page


class Goods(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        def proccess():
            goods_input = input.get("1.0", "end-1c")

            # Clear result files
            clear()

            if len(goods_input) < 1:
                messagebox.showerror(
                    title="Bermasalah!", message="Harap masukkan daftar barang yang Anda inginkan dengan benar!")
            elif goods_input.count(",") > 4:
                messagebox.showerror(
                    title="Bermasalah!", message="Harap masukkan daftar barang tidak lebih dari 5!")
            else:
                for i in goods_input.split(","):
                    goods.append(i.strip())
                    goods_result.append(extract_data(get_product_info(i.strip())[0]['data']['ace_search_product_v4']['data']['products'], i.strip()))

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

        default_url = "https://www.tokopedia.com/"

        def proccess():
            # Update product link
            data = result_data['recommendation']

            try:
                product_title_1.configure(command=lambda: webbrowser.open(data[0][8]))

                # Data produk pertama
                product_title_1.config(text=f"✅ {short(data[0][1])}")
                product_price_1.config(text=f"{short(data[0][5])}")
            except:
                print("=> Tidak terdapat produk pertama")

            try:
                product_title_2.configure(command=lambda: webbrowser.open(data[1][8]))

                # Data produk kedua
                product_title_2.config(text=f"✅ {short(data[1][1])}")
                product_price_2.config(text=f"{short(data[1][5])}")
            except:
                print("=> Tidak terdapat produk kedua")
                
            try:
                product_title_3.configure(command=lambda: webbrowser.open(data[2][8]))

                # Data produk ketiga
                product_title_3.config(text=f"✅ {short(data[2][1])}")
                product_price_3.config(text=f"{short(data[2][5])}")
            except:
                print("=> Tidak terdapat produk ketiga")

            try:
                product_title_4.configure(command=lambda: webbrowser.open(data[3][8]))

                # Data produk keempat
                product_title_4.config(text=f"✅ {short(data[3][1])}")
                product_price_4.config(text=f"{short(data[3][5])}")
            except:
                print("=> Tidak terdapat produk keempat")

            try:
                product_title_5.configure(command=lambda: webbrowser.open(data[4][8]))

                # Data produk kelima
                product_title_5.config(text=f"✅ {short(data[4][1])}")
                product_price_5.config(text=f"{short(data[4][5])}")
            except:
                print("=> Tidak terdapat produk kelima")
            
            price_amount = 0

            for i in data:
                price_amount += i[6]

            if price_amount > budget:
                message = f"(Anda membutuhkan tambahan sebesar Rp{thousand_format(price_amount-budget)})"
            elif price_amount < budget:
                message = f"(Anda untung sebesar Rp{thousand_format(budget-price_amount)})"
            else:
                message = f"(Budget Anda sesuai!)"

            total_price.config(text=f"Total: Rp{thousand_format(price_amount)} {message}")

        # Set background color white
        self.configure(background="white")

        # Budget
        title = Label(self, text="Angkost menemukan hasil:", font=Font(
            family="Montserrat Medium", size=22, weight="normal"), background="white")
        title.pack(pady=(30, 0), padx=20, side=tk.TOP, anchor="w")

        description = Label(self, text="Klik 'Tampilkan' untuk menampilkan barang rekomendasi kami. Hasil lain akan tersimpan di file angkost_result.xlsx", font=Font(
            family="Montserrat Medium", size=10), background="white", wraplength=540, justify="left", fg="#4F4F4F")
        description.pack(pady=(4, 0), padx=20, side=tk.TOP, anchor="w")

        product_title_1 = Button(self, text="❌ Produk #1", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white", borderwidth=0, command=lambda: webbrowser.open(default_url))
        product_title_1.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        product_price_1 = Label(self, text="Rp0", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        product_price_1.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        product_title_2 = Button(self, text="❌ Produk #2", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white", borderwidth=0, command=lambda: webbrowser.open(default_url))
        product_title_2.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        product_price_2 = Label(self, text="Rp0", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        product_price_2.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        product_title_3 = Button(self, text="❌ Produk #3", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white", borderwidth=0, command=lambda: webbrowser.open(default_url))
        product_title_3.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        product_price_3 = Label(self, text="Rp0", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        product_price_3.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        product_title_4 = Button(self, text="❌ Produk #4", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white", borderwidth=0, command=lambda: webbrowser.open(default_url))
        product_title_4.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        product_price_4 = Label(self, text="Rp0", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        product_price_4.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        product_title_5 = Button(self, text="❌ Produk #5", font=Font(
            family="Montserrat SemiBold", size=12, weight="normal"), fg="#353535", background="white", borderwidth=0, command=lambda: webbrowser.open(default_url))
        product_title_5.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        product_price_5 = Label(self, text="Rp0", font=Font(
            family="Montserrat Medium", size=10, weight="normal"), fg="#636262", background="white")
        product_price_5.pack(pady=(0, 0), padx=20, side=tk.TOP, anchor="w")

        total_price = Label(self, text="Total: Rp0", font=Font(
            family="Montserrat Regular", size=12, weight="normal"), fg="#333333", background="white")
        total_price.pack(pady=(20, 5), padx=20, side=tk.TOP, anchor="w")

        show_button = Button(self, text="Tampilkan", borderwidth=0,
                             bg="#525252", fg="white", command=proccess, width=16, height=1, font=Font(family="Montserrat Bold", size=12, weight="normal"))
        show_button.pack(pady=(30, 0))


# Driver Code
app = tkinterApp()

# Styling app
app.title("Angkost")
app.geometry("680x690")
app.resizable(False, True)
app.iconbitmap("./assets/angkost-icon.ico")
app.configure(background="white")

# Loop app
app.mainloop()
