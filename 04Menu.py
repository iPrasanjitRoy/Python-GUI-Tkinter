from tkinter import *

# Create The Main Window
root = Tk()

# Create A Menu Widget
menu = Menu(root)

# Set The Menu For The Root Window
root.config(menu=menu)

# Create A Cascading Menu (File)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

# Add Options To The File Menu
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()  # Add A Separator Line
filemenu.add_command(label="Exit", command=root.quit)

# Create Another Cascading Menu (Help)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

# Add An Option To The Help Menu
helpmenu.add_command(label="About")

# Run The Tkinter Event Loop
mainloop()
