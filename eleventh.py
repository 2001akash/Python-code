import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext

#creating tkinter main window
win=tk.Tk()
#title level
ttk.Label(win,text="ScrolledText For Python",font=("Times New Roman",15),background ="green",foreground ="white").grid (column=0,row=0)
win.mainloop()