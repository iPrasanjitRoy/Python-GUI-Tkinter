from tkinter import *
from tkinter import messagebox


def show_gender_message():
    if var1.get() == 1 and var2.get() == 0:
        message = "You Selected Male."
    elif var1.get() == 0 and var2.get() == 1:
        message = "You Selected Female."
    elif var1.get() == 1 and var2.get() == 1:
        message = "You Selected Both Male And Female."
    else:
        message = "Please Select A Gender."

    messagebox.showinfo("Gender Selection", message)


master = Tk()
master.title("Gender Selection")

var1 = IntVar()
Checkbutton(master, text="Male", variable=var1).grid(row=0, sticky=W)

var2 = IntVar()
Checkbutton(master, text="Female", variable=var2).grid(row=1, sticky=W)

# Button To Display The Selected Gender
Button(master, text="Show Gender", command=show_gender_message).grid(row=2, pady=10)

# To Get The Current Value Of Var1
value_of_var1 = var1.get()
print(value_of_var1)
value_of_var2 = var2.get()
print(value_of_var2)

mainloop()
