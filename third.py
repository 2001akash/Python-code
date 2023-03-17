from tkinter import *
root = Tk()
C = Canvas(root, bg="blue", height=1000, width=1000)
id=C.create_line(50,50,100,100,100,150, width=4, fill="white")
C.pack()
root.mainloop()