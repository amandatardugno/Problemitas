from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hola putazos").grid(column=0, row=0)
ttk.Button(frm, text=":)", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text=":(", command=root.destroy).grid(column=2, row=1)
root.mainloop()