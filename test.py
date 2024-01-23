from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hola esto es una prueba :)")
mainfr = ttk.Frame(root, padding = "3 3 12 12")
mainfr.grid(column = 0, row = 0, sticky = (N,W,E,S))
root.columconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)