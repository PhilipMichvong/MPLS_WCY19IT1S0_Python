#from PIL import ImageTk, Image
#from backend.controller import Controller
from tkinter import *
import tkinter as tk

import PIL.Image
import PIL.ImageTk
jpg_path = './frontend/assets/'


class GUI:
    JPG_PATH = "./frontend/assets/"

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.Console_Text = ""
        self.WindwowSettings("1280x720", "apka")
        self.ToolBox()
        self.MiddlePart()
        self.ConsoleOutputPart()

    def run(self):
        self.root.mainloop()

    def open_setings_r1(self, *args):
        set = tk.Tk()
        set.title(f"ustawienia router 1")
        set.geometry("365x300")
        consoleOutputLabel.config(text=">konfiguracja dla router 1")
        ip = tk.Label(set, text="interfejs:")
        ip.grid(row=0, column=1, padx=3)
        intr1 = tk.Entry(set)
        intr1.grid(row=1, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz ip:")
        ip.grid(row=2, column=1, padx=3)
        ipr1 = tk.Entry(set)
        ipr1.grid(row=3, column=1, padx=3)
        ip = tk.Label(set, text="wprowadz maske:")
        ip.grid(row=4, column=1, padx=3)
        maskr1 = tk.Entry(set)
        maskr1.grid(row=5, column=1, padx=3)

    # ustawienia do adresacji r2

    def open_setings_r2(self, *args):
        set = tk.Tk()
        set.title(f"ustawienia router 2")
        set.geometry("365x300")
        consoleOutputLabel.config(text=">konfiguracja dla router 1")
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

    # ustawienia do adresacji r3

    def open_setings_r3(self, *args):
        set = tk.Tk()
        set.title(f"ustawienia router 3")
        set.geometry("365x300")
        consoleOutputLabel.config(text=">konfiguracja dla router 1")
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

    # ustawienia do adresacji r4

    def open_setings_r4(self, *args):
        set = tk.Tk()
        set.title(f"ustawienia router 4")
        set.geometry("365x300")
        consoleOutputLabel.config(text=">konfiguracja dla router 1")
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

    # funkcja dodająca routery na przycisku

    def Router_Add(self):
        global img
        global img2
        global img3
        global img4

        img = PIL.ImageTk.PhotoImage(
            Image.open("./frontend/assets/rot.jpg", "rb"))
        img2 = PIL.ImageTk.PhotoImage(Image.open(
            "./frontend/assets/rot.jpg", "rb"))
        img3 = PIL.ImageTk.PhotoImage(Image.open(
            "./frontend/assets/rot.jpg", "rb"))
        img4 = PIL.ImageTk.PhotoImage(Image.open(
            "./frontend/assets/rot.jpg", "rb"))
        #global count_router

        label_router = Label(image=img)
        label_router.bind("<Button-1>", self.open_setings_r1)
        label_router.place(x=200, y=80)
        label2_router = Label(image=img2)
        label2_router.bind("<Button-1>", self.open_setings_r2)
        label2_router.place(x=760, y=80)
        label3_router = Label(image=img3)
        label3_router.bind("<Button-1>", self.open_setings_r3)
        label3_router.place(x=200, y=300)
        label4_router = Label(image=img4)
        label4_router.bind("<Button-1>", self.open_setings_r4)
        label4_router.place(x=760, y=300)
        consoleOutputLabel.config(
            text=f">Dodano routery, kliknij na nie aby skonfigurowac")

    def Computer_Add(self):
        global img_computer_1
        global img_computer_2
        global img_computer_3
        global img_computer_4

        consoleOutputLabel.config(
            text=f">Dodano Komputer - kliknij na nie aby skonfiguroawc")

        icon_size = Label()
        # #count_computer == 0:
        # if count_computer == 1:
        #     label_router = Label(image=img)
        #     label_router.place(x=140,y=80)
        # if count_computer == 2:
        #     label_router = Label(image=img)
        #     label_router.place(x=140, y=80)
        #     label2_router = Label(image=img2)
        #     label2_router.place(x=700, y=80)
        # if count_computer == 3:
        #     label_router = Label(image=img)
        #     label_router.place(x=140, y=80)
        #     label2_router = Label(image=img2)
        #     label2_router.place(x=700, y=80)
        #     label3_router = Label(image=img3)
        #     label3_router.place(x=140, y=300)
        #
        #
        # if count_computer == 4:
        #     label_router = Label(image=img)
        #     label_router.place(x=140, y=80)
        #     label2_router = Label(image=img2)
        #     label2_router.place(x=700, y=80)
        #     label3_router = Label(image=img3)
        #     label3_router.place(x=140, y=300)
        #     label4_router = Label(image=img4)
        #     label4_router.place(x=700, y=300)

    def WindwowSettings(self, resolution: str, title: str):
        self.root.geometry(resolution)
        self.root.title(title)
        self.root.resizable(False, False)

    def ToolBox(self):
        consoleLabel = tk.Label(self.root, text="Konsola symulacji",
                                font=('Arial', 15), fg="#32CD32")
        toolBoxLabel = tk.Label(self.root, text="ToolBox", font=('Arial', 15))
        RouterAddLabel = tk.Label(
            self.root, text="Dodaj Router", font=('Arial', 15))
        ComputerAddLabel = tk.Label(
            self.root, text="Dodaj komputer", font=('Arial', 15))
        RouterAddButton = tk.Button(self.root, text="router", font=(
            'arial', 10), command=lambda: self.Router_Add())
        ComputerAddButton = tk.Button(self.root, text="komputer", font=(
            'arial', 10), command=lambda: self.Computer_Add())
        MLTPlabel = tk.Label(
            self.root, text="Rozpocznij symulaje", font=('Arial', 14))
        MLTPbutton = tk.Button(self.root, text="MLTP", font=('arial', 10))
        CreditsLabel = tk.Label(self.root, text="""    Wykonali:
        Filip Szpregiel
        Bartlomiej Szykula
        Piotr Targowski
        """, font=('arial', 10))
        consoleLabel.place(x=500, y=510)
        toolBoxLabel.place(x=1129, y=30)
        RouterAddLabel.place(x=1110, y=150)
        ComputerAddLabel.place(x=1100, y=270)
        RouterAddButton.place(x=1120, y=200, width=100)
        ComputerAddButton.place(x=1120, y=320, width=100)
        CreditsLabel.place(x=1090, y=600)
        MLTPlabel.place(x=1080, y=400)
        MLTPbutton.place(x=1120, y=450, width=100)

    def MiddlePart(self):
        text = "MLTP symulator"
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
        Console_Text = ""
        global consoleOutputLabel
        consoleOutputLabel = tk.Label(
            self.root, text=Console_Text, font=('Arial', 8), fg="#FFF", bg="#000")
        consoleOutputLabel.clipboard_clear()
        consoleOutputLabel.place(x=40, y=570)
