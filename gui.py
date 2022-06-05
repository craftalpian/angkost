import requests as rs
import numpy as np
import tkinter as tk
from tkinter import ttk as ttk

class AngkostApp:
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # super().__init__()
        # self.root = tk.Tk(screenName="Angkost")
        # self.root.title("Angkost")
        # self.root.geometry("347x316")

    def home(self):
        frame = ttk.Frame(self.root)
        frame.grid()
        ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frame, text="Quit", command=self.home.destroy).grid(
            column=1, row=0)


# root = tk.Tk(screenName="Angkost")
# root.title("Angkost")
# root.geometry("347x316")
# frm = ttk.Frame(root, width=347, height=316)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
