import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    label = tk.Label(new_window, text="New Window")
    label.pack(padx=20, pady=20)

    # Button To Go Back
    back_button = tk.Button(new_window, text="Go Back", command=new_window.destroy)
    back_button.pack(pady=10)


# Main Tkinter Window
root = tk.Tk()
root.title("Main Window")

# Button To Open A New Window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=20)

# Run The Tkinter Event Loop
root.mainloop()
