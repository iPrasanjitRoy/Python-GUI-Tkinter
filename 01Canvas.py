import tkinter as tk


def draw_circle():
    canvas.create_oval(50, 50, 150, 150, fill="blue")


def draw_rectangle():
    canvas.create_rectangle(200, 50, 300, 150, fill="red")


def draw_line():
    canvas.create_line(350, 50, 450, 150, fill="green", width=2)


# Create The Main Window
root = tk.Tk()
root.title("Tkinter Canvas Example")

# Create A Canvas Widget
canvas = tk.Canvas(root, width=500, height=200)
canvas.pack()

# Create Buttons To Draw Shapes
circle_button = tk.Button(root, text="Draw Circle", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=10)

rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT, padx=10)

line_button = tk.Button(root, text="Draw Line", command=draw_line)
line_button.pack(side=tk.LEFT, padx=10)

# Run The Tkinter Event Loop
root.mainloop()
