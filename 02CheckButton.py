import tkinter as tk


def on_checkbutton_toggle():
    status_label.config(text="Checked" if check_var.get() else "Unchecked")


# Create The Main Window
root = tk.Tk()
root.title("Check Button Example")

# Create A Checkbutton And A Variable To Store Its State
check_var = tk.BooleanVar()
check_button = tk.Checkbutton(
    root, text="Check Me", variable=check_var, command=on_checkbutton_toggle
)
check_button.pack(pady=10)

# Create A Label To Display The Status Of The Check Button
status_label = tk.Label(root, text="Unchecked")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
