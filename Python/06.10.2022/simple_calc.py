from tkinter import *

root = Tk()
#root.geometry("200x300")
root.title("Calculator")
#root.resizable(False,False)

e = Entry(root, width=30, borderwidth=5)
e.grid(column=0, row=0, columnspan=4)

b7 = Button(text="7",padx=40, pady=40)
b7.grid(column=0, row=1)
b8 = Button(text="8",padx=40, pady=40)
b8.grid(column=1, row=1)
b9 = Button(text="9",padx=40, pady=40)
b9.grid(column=2, row=1)
bs = Button(text="<-",padx=40, pady=40)
bs.grid(column=3, row=1)

b4 = Button(text="4",padx=40, pady=40)
b4.grid(column=0, row=2)
b5 = Button(text="5",padx=40, pady=40)
b5.grid(column=1, row=2)
b6 = Button(text="6",padx=40, pady=40)
b6.grid(column=2, row=2)

b4 = Button(text="1",padx=40, pady=40)
b4.grid(column=0, row=3)
b5 = Button(text="2",padx=40, pady=40)
b5.grid(column=1, row=3)
b6 = Button(text="3",padx=40, pady=40)
b6.grid(column=2, row=3)

b0 = Button(text="0",padx=40, pady=40)
b0.grid(column=1, row=4)


root.mainloop()