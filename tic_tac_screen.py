from tkinter import *
from tkinter import ttk



root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
one = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
two = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
three = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)
four = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
five = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
six = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=1)
seven = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
eight = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
nine = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=2)

root.mainloop()
