from tkinter import *   

root = Tk()             
 
root.geometry('300x300')

def a():
    print("How are you")
 
btn = Button(root, text = 'exit', bd = '50',
                          command = root.destroy)
btn2=Button(root, text = 'Hello', bd = '50',
                          command = a)
btn.pack(side =LEFT) 
btn2.pack(side =LEFT)
 
root.mainloop()



