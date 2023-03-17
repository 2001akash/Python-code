#check
from tkinter import *
root= Tk()
root.geometry ("300x200")
w=Label (root,text='Python INT213',font ="58")
w.pack
Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()
Checkbutton4=IntVar()
Button1=Checkbutton(root,text="AKASH", variable = Checkbutton1,onvalue=1,offvalue =0,height=2,width=10)
Button2=Checkbutton(root,text="DEEP", variable = Checkbutton2,onvalue=1,offvalue =0,height=2,width=10)
Button3=Checkbutton(root,text="CSE", variable = Checkbutton3,onvalue=1,offvalue =0,height=2,width=10)
Button4=Checkbutton(root,text="LPU", variable = Checkbutton4,onvalue=1,offvalue =0,height=2,width=10)
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
root.mainloop()