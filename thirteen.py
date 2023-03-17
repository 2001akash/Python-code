from tkinter import *
def sel():
    x=val1.get()
    print("You Selected"+str(x))
root = Tk()

root.geometry("300x300")
frame1 = Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
frame1.grid(row=0,column=0)
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(frame1, tearoff=0)
frame = Frame(root, bg="red", highlightbackground="green", highlightthickness=5)
frame.grid(row=1,column=0)
label1=Label(frame, text="welcome to Python", width=20, height=2, font="Courier -10 bold underline", fg="blue", bg="yellow")
redbutton=Button(frame, text="Red", fg="red", bg="white")
redbutton.pack(side=LEFT)

val1=IntVar()
spin1=Spinbox(frame, from_=5, to=15, textvariable=val1, width=15, fg='blue', bg='yellow', font=('Arial',14,'bold'))
spin1.pack(side=LEFT)
val2=StringVar()
spin2=Spinbox(frame, values=('Hydrabad','Delhi','Kolkata','Mumbai'),
             textvariable=val2, width=15, fg='black',bg='yellow', font=('Arial',14,'bold'))
spin2.pack(side=LEFT)

root.mainloop()