import tkinter as tk 
root = tk.Tk() 
root.title('Title - button') 
my_button = tk.Button(root, text='HELLO', height=1, width=35, command=root.destroy) 
my_button.pack() 
root.mainloop()