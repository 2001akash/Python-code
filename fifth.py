from tkinter import *
root = Tk()
C = Canvas(root, bg="blue", height=1000, width=1000)
id=C.create_polygon(10, 10, 200, 200, 300, 200, width=3, fill="green", outline="red", smooth=1, activefill="lightblue")
C.pack()
root.mainloop()