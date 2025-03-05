import tkinter as tk
from tkinter import Entry
from typing import overload, override


class InputText (Entry):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas()
    def background_color(self,color:str):
        self.canvas.config(bg=color)
        self.config(bg=color)
    @override
    def grid_configure(self, cnf=None, **kw):
        self.grid(cnf, **kw)
        self.canvas.grid(cnf, **kw)
        grid = configure = config = self.grid_configure


def canvas_rounded_corners(radius, width, height, color, c: tk.Canvas):
    diameter = radius * 2
    c.create_oval(0, 0, diameter + 1, diameter + 1, fill=color, width=0)
    c.create_oval(width - diameter, 0, width - 1, diameter - 1, fill=color, width=0)
    c.create_oval(width - diameter, height - diameter, width - 1, height - 1, fill=color, width=0)
    c.create_oval(0, height - diameter, diameter - 1, height - 1, fill=color, width=0)
    c.create_polygon(radius, 0, width - radius, 0, width, radius, width, height - radius, width - radius, height,
                     radius, height, 0, height - radius, 0, radius, fill=color)

root = tk.Tk()
root.geometry("500x500")
root.configure()

root.grid_columnconfigure((0,1,2), weight=1, uniform='a')
root.grid_rowconfigure((0,1,2), weight=1, uniform='a')

container1 = tk.Canvas(background='red')
container2 = tk.Canvas(background='green')
container3 = tk.Canvas(background='blue')
container1.configure()
container1.grid(row=0,column=0)
container2.grid(row=1,column=1)
container3.grid(row=2,column=2)
ipn = InputText()
ipn.background_color('green')
ipn.grid(row=1, column=0)
ipn.configure(bg='blue')

root.mainloop()