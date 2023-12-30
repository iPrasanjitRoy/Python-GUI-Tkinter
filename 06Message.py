from tkinter import *

main = Tk()
ourMessage = "Hello World!"
messageVar = Message(main, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.pack()
main.mainloop()
