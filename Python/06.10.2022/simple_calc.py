from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False,False)

e = Entry(root, width=40, borderwidth=5)
e.grid(column=0, row=0, columnspan=4)

bprocent = Button(text="%", padx=20, pady=20)
bprocent.grid(column=0, row=1)
bce = Button(text="CE", padx=20, pady=20)
bce.grid(column=1, row=1)
bc = Button(text="C", padx=20, pady=20)
bc.grid(column=2, row=1)
bs = Button(text="<-", padx=20, pady=20)
bs.grid(column=3, row=1)

bulam = Button(text="1/x", padx=20, pady=20)
bulam.grid(column=0, row=2)
bpotega = Button(text="x²", padx=20, pady=20)
bpotega.grid(column=1, row=2)
bpierw = Button(text="√x", padx=20, pady=20)
bpierw.grid(column=2, row=2)
bdziel = Button(text="/", padx=20, pady=20)
bdziel.grid(column=3, row=2)

b7 = Button(text="7",padx=20, pady=20, )
b7.grid(column=0, row=3)
b8 = Button(text="8",padx=20, pady=20)
b8.grid(column=1, row=3)
b9 = Button(text="9",padx=20, pady=20)
b9.grid(column=2, row=3)
bx = Button(text="X",padx=20, pady=20)
bx.grid(column=3, row=3)

b4 = Button(text="4",padx=20, pady=20)
b4.grid(column=0, row=4)
b5 = Button(text="5",padx=20, pady=20)
b5.grid(column=1, row=4)
b6 = Button(text="6",padx=20, pady=20)
b6.grid(column=2, row=4)
bminus = Button(text="-",padx=20, pady=20)
bminus.grid(column=3, row=4)

b4 = Button(text="1",padx=20, pady=20)
b4.grid(column=0, row=5)
b5 = Button(text="2",padx=20, pady=20)
b5.grid(column=1, row=5)
b6 = Button(text="3",padx=20, pady=20)
b6.grid(column=2, row=5)
bplus = Button(text="+",padx=20, pady=20)
bplus.grid(column=3, row=5)

bpm = Button(text="+/-",padx=20, pady=20)
bpm.grid(column=0, row=6)
b0 = Button(text="0",padx=20, pady=20)
b0.grid(column=1, row=6)
bprzecinek = Button(text=",",padx=20, pady=20)
bprzecinek.grid(column=2, row=6)
brownaj = Button(text="=",padx=20, pady=20)
brownaj.grid(column=3, row=6)

root.mainloop()
