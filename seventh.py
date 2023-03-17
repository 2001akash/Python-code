from tkinter import *
root = Tk()
C = Canvas(root, bg="blue", height=1000, width=1000)
id=C.create_text(500, 100, text="My canvas", fill="yellow",activefill="lightblue")
C.pack()
root.mainloop()
