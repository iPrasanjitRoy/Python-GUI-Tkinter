import tkinter as tk


def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        status_label.config(text=f"Selected Item: {selected_item}")
    else:
        status_label.config(text="No Item Selected")


# Create The Main Window
root = tk.Tk()
root.title("Listbox Example")

# Create A Listbox
listbox = tk.Listbox(
    root, selectmode=tk.SINGLE
)  # Use tk.MULTIPLE For Multiple Selections
listbox.pack(pady=10)

# Insert Items Into The Listbox
for item in ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]:
    listbox.insert(tk.END, item)  # # Insert Items At The End Of The List

# Bind The On_Select Function To The Listbox Selection Event
# Bind: This Method Is Used To Associate An Event With A Function
# ListBoxSelect: Denotes The Event You're Interested In, Specifically When An Item Is Selected In The Listbox
# On_Select: Refers To The Function That Should Be Executed When The Specified Event Occurs
listbox.bind("<<ListboxSelect>>", on_select)

# Create A Label To Display The Selected Item
status_label = tk.Label(root, text="No Item Selected")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
