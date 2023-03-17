from tkinter import *
root = Tk()
root.geometry("300x300")
frame = Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
frame.grid(row=0,column=0)
redbutton=Button(frame, text="Red", fg="red", bg="white")
bluebutton=Button(frame, text="blue", fg="blue", bg="white")
pinkbutton=Button(frame, text="pink", fg="pink", bg="white")
blackbutton=Button(frame, text="black", fg="black", bg="white")

redbutton.pack(side=RIGHT)
bluebutton.pack(side=LEFT)
pinkbutton.pack(side=LEFT)
blackbutton.pack(side=LEFT)

root.mainloop()