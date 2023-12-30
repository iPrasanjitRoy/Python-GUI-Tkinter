import tkinter as tk


def menu_command():
    print("Menu Item Clicked!")


root = tk.Tk()

mb = tk.Menubutton(root, text="Select Option", relief=tk.RAISED)
mb.grid()

menu = tk.Menu(mb)
mb["menu"] = menu

menu.add_command(label="Option 1", command=menu_command)
menu.add_command(label="Option 2", command=menu_command)
menu.add_separator()
menu.add_command(label="Option 3", command=menu_command)

root.mainloop()
