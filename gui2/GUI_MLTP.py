import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


root = tk.Tk()

global Console_Text

count_computer = 0
count_router = 0


def open_setings_r1(*args):
    set = tk.Tk()
    set.title(f"ustawienia router 1")
    set.geometry("365x300")
    consoleOutputLabel.config(text=">konfiguracja dla router 1")
    ip = tk.Label(set,text="interfejs:")
    ip.grid(row=0,column=1,padx=3)
    input_ip = tk.Entry(set)
    input_ip.grid(row=1, column=1, padx=3)
    ip = tk.Label(set, text="wprowadz ip:")
    ip.grid(row=2, column=1, padx=3)
    input_ip = tk.Entry(set)
    input_ip.grid(row=3, column=1, padx=3)
    ip = tk.Label(set, text="wprowadz maske:")
    ip.grid(row=4, column=1, padx=3)
    input_ip = tk.Entry(set)
    input_ip.grid(row=5, column=1, padx=3)
    
    
def Router_Add():
    global img
    global img2
    global img3
    global img4

    img = ImageTk.PhotoImage(Image.open("rot.jpg"))
    img2 = ImageTk.PhotoImage(Image.open("rot.jpg"))
    img3 = ImageTk.PhotoImage(Image.open("rot.jpg"))
    img4 = ImageTk.PhotoImage(Image.open("rot.jpg"))
    #global count_router

    label_router = Label(image=img)
    label_router.bind("<Button-1>", open_setings_r1)
    label_router.place(x=200, y=80)
    label2_router = Label(image=img2)
    label2_router.place(x=760, y=80)
    label3_router = Label(image=img3)
    label3_router.place(x=200, y=300)
    label4_router = Label(image=img4)
    label4_router.place(x=760, y=300)
    consoleOutputLabel.config(text=f">Dodano routery, kliknij na nie aby skonfigurowac")
    
    
def Computer_Add():
    global img_computer_1
    global img_computer_2
    global img_computer_3
    global img_computer_4

    consoleOutputLabel.config(text=f">Dodano Komputer - kliknij na nie aby skonfiguroawc")

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


def WindwowSettings(resolution: str, title: str):
    root.geometry(resolution)
    root.title(title)
    root.resizable(False, False)


def ToolBox():
    consoleLabel = tk.Label(root, text="Konsola symulacji", font=('Arial', 15), fg="#32CD32")
    toolBoxLabel = tk.Label(root, text="ToolBox", font=('Arial', 15))
    RouterAddLabel = tk.Label(root, text="Dodaj Router", font=('Arial', 15))
    ComputerAddLabel = tk.Label(root, text="Dodaj komputer", font=('Arial', 15))
    RouterAddButton = tk.Button(root, text="router", font=('arial', 10), command=lambda: Router_Add())
    ComputerAddButton = tk.Button(root, text="komputer", font=('arial', 10), command=lambda: Computer_Add())
    MLTPlabel = tk.Label(root, text="Rozpocznij symulaje", font=('Arial', 14))
    MLTPbutton = tk.Button(root, text="MLTP", font=('arial', 10))
    CreditsLabel = tk.Label(root, text="""    Wykonali:
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
    MLTPbutton.place(x=1120, y=450,width=100)


def MiddlePart():
    text = "MLTP symulator"
    label = tk.Label(root, text=text, font=('Arial', 20))
    label.place(x=460, y=10)
    canvas_rectangle = Canvas(root, width=1050, height=450)
    canvas_rectangle.create_rectangle(0, 10, 1020, 450, outline="#FFF", fill="#FFF")
    canvas_rectangle.place(x=30, y=50)


def ConsoleOutputPart():
    console_canvas_rectangle = Canvas(root, width=1050, height=200)
    console_canvas_rectangle.create_rectangle(0, 10, 1020, 150, outline="#FFF", fill="#000")
    console_canvas_rectangle.place(x=30, y=550)
    Console_Text = ""
    global consoleOutputLabel
    consoleOutputLabel = tk.Label(root, text=Console_Text, font=('Arial', 8), fg="#FFF", bg="#000")
    consoleOutputLabel.clipboard_clear()
    consoleOutputLabel.place(x=40, y=570)


WindwowSettings("1280x720", "apka")

ToolBox()

MiddlePart()

ConsoleOutputPart()

root.mainloop()
