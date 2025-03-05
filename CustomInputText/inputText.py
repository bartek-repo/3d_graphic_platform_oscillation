import tkinter as tk
from tkinter import font, Frame, Entry
from typing import  override
import math as math

def canvas_rounded_corners(radius, width, height, color, c: tk.Canvas):
    diameter = radius * 2
    c.create_oval(0, 0, diameter + 1, diameter + 1, fill=color, width=0)
    c.create_oval(width - diameter, 0, width - 1, diameter - 1, fill=color, width=0)
    c.create_oval(width - diameter, height - diameter, width - 1, height - 1, fill=color, width=0)
    c.create_oval(0, height - diameter, diameter - 1, height - 1, fill=color, width=0)
    c.create_polygon(radius, 0, width - radius, 0, width, radius, width, height - radius, width - radius, height,
                     radius, height, 0, height - radius, 0, radius, fill=color)

class InputText (Frame):
    def __init__(self,parent,font,color='white'):
        tk.Frame.__init__(self,parent)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.input = Entry(self,bg=color,font=font)
        self.rounded = tk.Canvas(self,bg=color)
        self.input.grid(row=0,column=0)
        self.input.lift()
        self.rounded.grid(row=0,column=0)

root = tk.Tk()
root.geometry("500x500")
root.configure()

root.grid_columnconfigure((0,1,2), weight=1, uniform='a')
root.grid_rowconfigure((0,1,2), weight=1, uniform='a')

container1 = tk.Canvas(background='red')
container2 = tk.Canvas(background='green')
container3 = tk.Canvas(background='blue')

container1.grid(row=0,column=0)
container2.grid(row=1,column=1)
container3.grid(row=2,column=2)
root.update()

ipn = InputText(parent = root,font=font.Font(family="Times New Roman",size=8),color='black')
ipn.grid(row=1,column=0)


root.mainloop()