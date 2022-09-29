from re import T
from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Aplikacja")
window.minsize(width=500, height=500)

#label text value

lbl = Label(text="Pierwsza Etykieta")
lbl2 = Label(text="Druga Etykieta")
lbl["text"] = "Nowa wartość etykiety marchew"
lbl.pack()
lbl2.pack()
lbl2.config(text="Nowy tekst drugiej etykiety brzoskwinia")

#buttons

def btn_clicked():
    lbl.config(text=e.get(), font="Arial")

def btn2_clicked():
    exit()

btn=Button()
btn.config(text="CliCk me", command=btn_clicked)
btn.pack()
btn2=Button()
btn2.config(text="Close app", command=btn2_clicked)
btn2.pack()

#entry (inputs)

e = Entry(width=30)
e.pack(side="left")


window.mainloop()