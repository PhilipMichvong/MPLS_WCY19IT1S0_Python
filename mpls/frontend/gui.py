#from PIL import ImageTk, Image
#from backend.controller import Controller
from tkinter import *
import tkinter as tk
import os
import PIL.Image
import PIL.ImageTk
import pathlib
import time

from backend.controller import Controller as Ctlr

jpg_path = './frontend/assets/'


class GUI:
    JPG_PATH = "./frontend/assets/"

    def __init__(self) -> None:
        self.root = tk.Tk()

        self.console_lines = []
        self.console_lines_max = 7

        self.WindwowSettings("1280x720", "MPLS simulator MAST")
        self.ToolBox()
        self.MiddlePart()
        self.consoleOutputLabel = self.ConsoleOutputPart()

    def run(self):
        self.root.mainloop()

    def console_log(self, text: str):
        self.console_lines.append(text)
        if len(self.console_lines) > self.console_lines_max:
            self.console_lines.pop(0)

        text = ""
        for log in self.console_lines:
            text = text + log + '\n'

        self.consoleOutputLabel.config(text=text)

    def open_setings_r1(self, *args):
        set = tk.Tk()
        set.title(f"ustawienia router 1")
        set.geometry("600x300")
        # self.consoleOutputLabel.config(text=">konfiguracja dla router 1")
        ip = tk.Label(set, text="interfejs:")
        ip.grid(row=0, column=1, padx=3)
        global intr1
        intr1 = tk.Entry(set)
        intr1.grid(row=1, column=1, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(0, 'interface', 0))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(0, 'address', 0))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(0, 'mask', 0))
        mask_text.grid(row=6, column=2, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=3, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(0, 'interface', 1))
        int_text.grid(row=2, column=3, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=3, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(0, 'address', 1))
        ip_text.grid(row=4, column=3, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=3, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(0, 'mask', 1))
        mask_text.grid(row=6, column=3, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=4, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(0, 'interface', 2))
        int_text.grid(row=2, column=4, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=4, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(0, 'address', 2))
        ip_text.grid(row=4, column=4, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=4, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(0, 'mask', 2))
        mask_text.grid(row=6, column=4, padx=3)

        ip = tk.Label(set, text="wprowadz ip:")
        ip.grid(row=2, column=1, padx=3)
        global ipr1
        ipr1 = tk.Entry(set)
        ipr1.grid(row=3, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz maske:")
        ip.grid(row=4, column=1, padx=3)
        global maskr1
        maskr1 = tk.Entry(set)
        maskr1.grid(row=5, column=1, padx=3)

        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.add_interface(self, 0, intr1.get(), ipr1.get(), maskr1.get()))

        ApplyButton.grid(row=6, column=1)

    def open_setings_r2(self, *args):
        global intr2, ipr2, maskr2
        set = tk.Tk()
        set.title(f"ustawienia router 2")
        set.geometry("600x300")
        # self.consoleOutputLabel.config(text=">konfiguracja dla router 1")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(1, 'interface', 0))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(1, 'address', 0))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(1, 'mask', 0))
        mask_text.grid(row=6, column=2, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=3, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(1, 'interface', 1))
        int_text.grid(row=2, column=3, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=3, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(1, 'address', 1))
        ip_text.grid(row=4, column=3, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=3, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(1, 'mask', 1))
        mask_text.grid(row=6, column=3, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=4, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(1, 'interface', 2))
        int_text.grid(row=2, column=4, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=4, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(1, 'address', 2))
        ip_text.grid(row=4, column=4, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=4, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(1, 'mask', 2))
        mask_text.grid(row=6, column=4, padx=3)

        ip = tk.Label(set, text="interfejs:")
        ip.grid(row=0, column=1, padx=3)
        intr2 = tk.Entry(set)
        intr2.grid(row=1, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz ip:")
        ip.grid(row=2, column=1, padx=3)
        ipr2 = tk.Entry(set)
        ipr2.grid(row=3, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz maske:")
        ip.grid(row=4, column=1, padx=3)
        maskr2 = tk.Entry(set)
        maskr2.grid(row=5, column=1, padx=3)
        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.add_interface(self, 1, intr2.get(), ipr2.get(), maskr2.get()))
        ApplyButton.grid(row=6, column=1)

    def open_setings_r3(self, *args):
        global intr3, ipr3, maskr3
        set = tk.Tk()
        set.title(f"ustawienia router 3")
        set.geometry("600x300")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(1, 'interface', 0))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(1, 'address', 0))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(1, 'mask', 0))
        mask_text.grid(row=6, column=2, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=3, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(2, 'interface', 1))
        int_text.grid(row=2, column=3, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=3, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(2, 'address', 1))
        ip_text.grid(row=4, column=3, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=3, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(2, 'mask', 1))
        mask_text.grid(row=6, column=3, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=4, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(2, 'interface', 2))
        int_text.grid(row=2, column=4, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=4, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(2, 'address', 2))
        ip_text.grid(row=4, column=4, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=4, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(2, 'mask', 2))
        mask_text.grid(row=6, column=4, padx=3)

        # self.consoleOutputLabel.config(text=">konfiguracja dla router 1")
        ip = tk.Label(set, text="interfejs:")
        ip.grid(row=0, column=1, padx=3)
        intr3 = tk.Entry(set)
        intr3.grid(row=1, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz ip:")
        ip.grid(row=2, column=1, padx=3)
        ipr3 = tk.Entry(set)
        ipr3.grid(row=3, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz maske:")
        ip.grid(row=4, column=1, padx=3)
        maskr3 = tk.Entry(set)
        maskr3.grid(row=5, column=1, padx=3)
        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.add_interface(self, 2, intr3.get(), ipr3.get(), maskr3.get()))
        ApplyButton.grid(row=6, column=1)

    def open_setings_r4(self, *args):
        global intr4, ipr4, maskr4
        set = tk.Tk()
        set.title(f"ustawienia router 4")
        set.geometry("600x300")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(3, 'interface', 0))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(3, 'address', 0))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(3, 'mask', 0))
        mask_text.grid(row=6, column=2, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=3, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(3, 'interface', 1))
        int_text.grid(row=2, column=3, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=3, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(3, 'address', 1))
        ip_text.grid(row=4, column=3, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=3, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(3, 'mask', 1))
        mask_text.grid(row=6, column=3, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=4, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(3, 'interface', 2))
        int_text.grid(row=2, column=4, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=4, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(3, 'address', 2))
        ip_text.grid(row=4, column=4, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=4, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(3, 'mask', 2))
        mask_text.grid(row=6, column=4, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(2, 'interface', 0))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(2, 'address', 0))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(2, 'mask', 0))
        mask_text.grid(row=6, column=2, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=3, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(2, 'interface', 1))
        int_text.grid(row=2, column=3, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=3, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(2, 'address', 1))
        ip_text.grid(row=4, column=3, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=3, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(2, 'mask', 1))
        mask_text.grid(row=6, column=3, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=4, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_router_data(2, 'interface', 2))
        int_text.grid(row=2, column=4, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=4, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_router_data(2, 'address', 2))
        ip_text.grid(row=4, column=4, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=4, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_router_data(2, 'mask', 2))
        mask_text.grid(row=6, column=4, padx=3)

        # self.consoleOutputLabel.config(text=">konfiguracja dla router 1")
        ip = tk.Label(set, text="interfejs:")
        ip.grid(row=0, column=1, padx=3)
        intr4 = tk.Entry(set)
        intr4.grid(row=1, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz ip:")
        ip.grid(row=2, column=1, padx=3)
        ipr4 = tk.Entry(set)
        ipr4.grid(row=3, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz maske:")
        ip.grid(row=4, column=1, padx=3)
        maskr4 = tk.Entry(set)
        maskr4.grid(row=5, column=1, padx=3)
        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.add_interface(self, 3, intr4.get(), ipr4.get(), maskr4.get()))
        ApplyButton.grid(row=6, column=1)

    def open_setings_c1(self, *args):
        set = tk.Tk()
        set.title("ustawienia komputera 1")
        set.geometry("400x300")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_pc_data(0, 'interface'))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_pc_data(0, 'address'))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(0, 'mask'))
        mask_text.grid(row=6, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Brama domyślna:")
        mask_text_label.grid(row=7, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(0, 'gateway'))
        mask_text.grid(row=8, column=2, padx=3)

        title = tk.Label(set, text="brama:")
        title.grid(row=0, column=1, padx=3)
        gateway1 = tk.Entry(set)
        gateway1.grid(row=1, column=1, padx=3)

        title = tk.Label(set, text="ip:")
        title.grid(row=2, column=1, padx=3)
        ip_pc1 = tk.Entry(set)
        ip_pc1.grid(row=3, column=1, padx=3)

        title = tk.Label(set, text="maska:")
        title.grid(row=4, column=1, padx=3)
        mask_pc1 = tk.Entry(set)
        mask_pc1.grid(row=5, column=1, padx=3)

        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.pc_configure(self, 0, gateway1.get(), ip_pc1.get(), mask_pc1.get()))
        ApplyButton.grid(row=7, column=1)

    def open_setings_c2(self, *args):
        set = tk.Tk()
        set.title("ustawienia komputera 2")
        set.geometry("400x300")
        title = tk.Label(set, text="brama:")
        title.grid(row=0, column=1, padx=3)
        gateway2 = tk.Entry(set)
        gateway2.grid(row=1, column=1, padx=3)

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_pc_data(1, 'interface'))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_pc_data(1, 'address'))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(1, 'mask'))
        mask_text.grid(row=6, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Brama domyślna:")
        mask_text_label.grid(row=7, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(1, 'gateway'))
        mask_text.grid(row=8, column=2, padx=3)

        title = tk.Label(set, text="ip:")
        title.grid(row=2, column=1, padx=3)
        ip_pc2 = tk.Entry(set)
        ip_pc2.grid(row=3, column=1, padx=3)

        title = tk.Label(set, text="maska:")
        title.grid(row=4, column=1, padx=3)
        mask_pc2 = tk.Entry(set)
        mask_pc2.grid(row=5, column=1, padx=3)
        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.pc_configure(self, 1, gateway2.get(), ip_pc2.get(), mask_pc2.get()))
        ApplyButton.grid(row=7, column=1)

    def open_setings_c3(self, *args):
        set = tk.Tk()
        set.title("ustawienia komputera 3")
        set.geometry("400x300")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_pc_data(2, 'interface'))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_pc_data(2, 'address'))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(2, 'mask'))
        mask_text.grid(row=6, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Brama domyślna:")
        mask_text_label.grid(row=7, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(2, 'gateway'))
        mask_text.grid(row=8, column=2, padx=3)

        title = tk.Label(set, text="brama:")
        title.grid(row=0, column=1, padx=3)
        gateway3 = tk.Entry(set)
        gateway3.grid(row=1, column=1, padx=3)

        title = tk.Label(set, text="ip:")
        title.grid(row=2, column=1, padx=3)
        ip_pc3 = tk.Entry(set)
        ip_pc3.grid(row=3, column=1, padx=3)

        title = tk.Label(set, text="maska:")
        title.grid(row=4, column=1, padx=3)
        mask_pc3 = tk.Entry(set)
        mask_pc3.grid(row=5, column=1, padx=3)
        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.pc_configure(self, 2, gateway3.get(), ip_pc3.get(), mask_pc3.get()))
        ApplyButton.grid(row=7, column=1)

    def open_setings_c4(self, *args):
        set = tk.Tk()
        set.title("ustawienia komputera 4")
        set.geometry("400x300")

        int_text_label = tk.Label(set, text="Interfejs:")
        int_text_label.grid(row=1, column=2, padx=3)
        int_text = tk.Label(set, text=Ctlr.get_pc_data(3, 'interface'))
        int_text.grid(row=2, column=2, padx=3)

        ip_text_label = tk.Label(set, text="Adres:")
        ip_text_label.grid(row=3, column=2, padx=3)
        ip_text = tk.Label(set, text=Ctlr.get_pc_data(3, 'address'))
        ip_text.grid(row=4, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Maska:")
        mask_text_label.grid(row=5, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(3, 'mask'))
        mask_text.grid(row=6, column=2, padx=3)

        mask_text_label = tk.Label(set, text="Brama domyślna:")
        mask_text_label.grid(row=7, column=2, padx=3)
        mask_text = tk.Label(set, text=Ctlr.get_pc_data(3, 'gateway'))
        mask_text.grid(row=8, column=2, padx=3)

        title = tk.Label(set, text="brama:")
        title.grid(row=0, column=1, padx=3)
        gateway4 = tk.Entry(set)
        gateway4.grid(row=1, column=1, padx=3)

        title = tk.Label(set, text="ip:")
        title.grid(row=2, column=1, padx=3)
        ip_pc4 = tk.Entry(set)
        ip_pc4.grid(row=3, column=1, padx=3)

        title = tk.Label(set, text="maska:")
        title.grid(row=4, column=1, padx=3)
        mask_pc4 = tk.Entry(set)
        mask_pc4.grid(row=5, column=1, padx=3)

        ApplyButton = tk.Button(set, text="Zatwiedz", font=(
            'arial', 10), command=lambda: Ctlr.pc_configure(self, 3, gateway4.get(), ip_pc4.get(), mask_pc4.get()))
        ApplyButton.grid(row=7, column=1)

    def MPLS(self):
        Ctlr.integration_tests(self)

    def Devices_add(self):
        self.Computer_Add()
        self.Router_Add()

    def Router_Add(self):
        global photo1, photo2, photo3, photo4

        jpg_path = pathlib.Path.absolute(
            pathlib.Path('.\\frontend\\rot.jpg')
        )
        img = PIL.Image.open(
            jpg_path)
        img2 = PIL.Image.open(
            jpg_path)
        img3 = PIL.Image.open(
            jpg_path)
        img4 = PIL.Image.open(
            jpg_path)
        photo1 = PIL.ImageTk.PhotoImage(img)
        photo2 = PIL.ImageTk.PhotoImage(img2)
        photo3 = PIL.ImageTk.PhotoImage(img3)
        photo4 = PIL.ImageTk.PhotoImage(img4)
        #global count_router

        label_router = Label(image=photo1)
        label_router.bind("<Button-1>", self.open_setings_r1)
        label_router.place(x=200, y=80)
        label2_router = Label(image=photo2)
        label2_router.bind("<Button-1>", self.open_setings_r2)
        label2_router.place(x=760, y=80)
        label3_router = Label(image=photo3)
        label3_router.bind("<Button-1>", self.open_setings_r3)
        label3_router.place(x=200, y=300)
        label4_router = Label(image=photo4)
        label4_router.bind("<Button-1>", self.open_setings_r4)
        label4_router.place(x=760, y=300)

        Ctlr.routers_add(self)

    def Computer_Add(self):
        global photo1_cmp
        global photo2_cmp
        global photo3_cmp
        global photo4_cmp
        jpg_path_comp = pathlib.Path.absolute(
            pathlib.Path('.\\frontend\\computer.jpg')
        )
        img_comp = PIL.Image.open(
            jpg_path_comp)
        img2_comp = PIL.Image.open(
            jpg_path_comp)
        img3_comp = PIL.Image.open(
            jpg_path_comp)
        img4_comp = PIL.Image.open(
            jpg_path_comp)
        photo1_cmp = PIL.ImageTk.PhotoImage(img_comp)
        photo2_cmp = PIL.ImageTk.PhotoImage(img2_comp)
        photo3_cmp = PIL.ImageTk.PhotoImage(img3_comp)
        photo4_cmp = PIL.ImageTk.PhotoImage(img4_comp)

        label_comp = Label(image=photo1_cmp)
        label_comp.bind("<Button-1>", self.open_setings_c1)
        label_comp.place(x=100, y=80)
        label_comp2 = Label(image=photo1_cmp)
        label_comp2.bind("<Button-1>", self.open_setings_c2)
        label_comp2.place(x=840, y=80)
        label_comp3 = Label(image=photo1_cmp)
        label_comp3.bind("<Button-1>", self.open_setings_c3)
        label_comp3.place(x=100, y=300)
        label_comp4 = Label(image=photo1_cmp)
        label_comp4.bind("<Button-1>", self.open_setings_c4)
        label_comp4.place(x=840, y=300)

        Ctlr.pcs_add(self)

    def WindwowSettings(self, resolution: str, title: str):
        self.root.geometry(resolution)
        self.root.title(title)
        self.root.resizable(False, False)

    def ToolBox(self):
        consoleLabel = tk.Label(self.root, text="Konsola symulacji",
                                font=('Arial', 15), fg="#32CD32")
        toolBoxLabel = tk.Label(self.root, text="ToolBox", font=('Arial', 15))
        DevicesAddLabel = tk.Label(
            self.root, text="Dodaj urządzenia", font=('Arial', 14))
        load_conf_label = tk.Label(
            self.root, text="Wgraj konfigurację", font=('Arial', 14))
        DeviceAddButton = tk.Button(self.root, text="Dodaj", font=(
            'arial', 10), command=lambda: self.Devices_add())
        MLTPlabel = tk.Label(
            self.root, text="Rozpocznij symulaje", font=('Arial', 14))
        MLTPbutton = tk.Button(self.root, text="MPLS", font=(
            'arial', 10), command=lambda: self.MPLS())
        CreditsLabel = tk.Label(self.root, text="""    Wykonali:
        Filip Szpregiel
        Bartlomiej Szykula
        Piotr Targowski
        """, font=('arial', 10))

        load_conf = tk.Button(self.root, text="Wgraj", font=('Arial', 10),
                              command=lambda: Ctlr.load_default_config(self))
        consoleLabel.place(x=500, y=510)
        toolBoxLabel.place(x=1129, y=30)
        DevicesAddLabel.place(x=1100, y=250)
        DeviceAddButton.place(x=1120, y=300, width=100)
        CreditsLabel.place(x=1090, y=600)
        MLTPlabel.place(x=1080, y=400)
        MLTPbutton.place(x=1120, y=450, width=100)
        load_conf.place(x=1150, y=150)
        load_conf_label.place(x=1094, y=100)

    def MiddlePart(self):
        text = "MPLS symulator"
        label = tk.Label(self.root, text=text, font=('Arial', 20))
        label.place(x=460, y=10)
        canvas_rectangle = Canvas(self.root, width=1050, height=450)
        canvas_rectangle.create_rectangle(
            0, 10, 1020, 450, outline="#FFF", fill="#FFF")
        canvas_rectangle.place(x=30, y=50)

    def ConsoleOutputPart(self):
        console_canvas_rectangle = Canvas(self.root, width=1050, height=200)
        console_canvas_rectangle.create_rectangle(
            0, 10, 1020, 150, outline="#FFF", fill="#000")
        console_canvas_rectangle.place(x=30, y=550)
        consoleOutputLabel = tk.Label(
            self.root, text="", font=('Arial', 8), fg="#FFF", bg="#000")
        consoleOutputLabel.clipboard_clear()
        consoleOutputLabel.place(x=40, y=570)
        return consoleOutputLabel
