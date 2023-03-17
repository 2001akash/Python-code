import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    text="HELLO EVERYONE",
    variable=my_boolean_var
)
my_checkbutton.pack()
root.mainloop()