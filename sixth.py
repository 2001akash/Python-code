from tkinter import *
root = Tk()
C = Canvas(root, bg="blue", height=1000, width=1000)
id=C.create_rectangle(500, 200, 700, 600, width=2, fill="yellow", outline="red", activefill="lightblue")
C.pack()
root.mainloop()
