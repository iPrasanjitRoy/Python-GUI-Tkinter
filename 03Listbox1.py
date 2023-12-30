import tkinter as tk


def on_select(event):
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(index) for index in selected_indices]
    if selected_items:
        status_label.config(text=f"Selected Items: {', '.join(selected_items)}")
    else:
        status_label.config(text="No Items Selected")


# Create The Main Window
root = tk.Tk()
root.title("Listbox Example - Multiple Selections")

# Create A Listbox With Multiple Selection Mode
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

# Insert Items Into The Listbox
for item in ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]:
    listbox.insert(tk.END, item)

# Bind The On_Select Function To The Listbox Selection Event
listbox.bind("<<ListboxSelect>>", on_select)

# Create A Label To Display The Selected Items
status_label = tk.Label(root, text="No Items Selected")
status_label.pack(pady=10)

# Run The Tkinter Event Loop
root.mainloop()
