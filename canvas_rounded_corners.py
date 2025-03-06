import tkinter as tk


def canvas_rounded_corners(radius, width, height, color, c: tk.Canvas):
    diameter = radius * 2
    c.create_oval(0, 0, diameter + 1, diameter + 1, fill=color, width=0)
    c.create_oval(width - diameter, 0, width - 1, diameter - 1, fill=color, width=0)
    c.create_oval(width - diameter, height - diameter, width - 1, height - 1, fill=color, width=0)
    c.create_oval(0, height - diameter, diameter - 1, height - 1, fill=color, width=0)
    c.create_polygon(radius, 0, width - radius, 0, width, radius, width, height - radius, width - radius, height,
                     radius, height, 0, height - radius, 0, radius, fill=color)