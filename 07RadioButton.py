from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text="1", variable=v, value=1).pack()
Radiobutton(root, text="2", variable=v, value=2).pack()
mainloop()
