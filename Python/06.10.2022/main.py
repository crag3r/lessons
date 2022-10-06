from tkinter import *

window = Tk()
window.title("Nowe okienko")
window.resizable(False,False)
window.geometry("512x512")

def change_lbl():
    lbl.config(text=e.get())

lbl = Label()
lbl.config(text="Nowa etykieta", font=("Calibri",24))
lbl.grid(column=0,row=0)

e = Entry()
e.config(width=50)
e.grid(column=0,row=1)

btn = Button()
btn.config(text="Klikaj mnie", command=change_lbl)
btn.grid(column=1, row=1, ipadx=10, ipady=10)



window.mainloop()

