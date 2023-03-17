from tkinter import *
root = Tk()
C = Canvas(root, bg="blue", height=1000, width=1000)
id=C.create_oval(100,100,400,300, width=5, fill="yellow", outline="red", activefill="lightblue")
C.pack()
root.mainloop()