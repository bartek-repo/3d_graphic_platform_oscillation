from tkinter import Frame, Entry
from canvas_rounded_corners import *



class InputText (Frame):
    def __init__(self,parent,font,color='white',backgroundcolor='black',
                 fontcolor='black',radius=0):

        tk.Frame.__init__(self,parent)

        #create main property
        self.radius=radius
        self.color = color

        #help value
        x = radius-radius/pow(2,1/2)

        self.rowconfigure(0,weight=1,uniform='a')
        self.columnconfigure(0,weight=1,uniform='a')

        self.can = tk.Canvas(self,background=backgroundcolor,highlightthickness=0)
        self.inp = Entry(self,background=color,borderwidth=0,foreground=fontcolor, font = font)

        #fill all, and add pad to corners
        self.can.grid(row=0,column=0,sticky='nswe')
        self.inp.grid(row=0,column=0,padx=x,pady=x,sticky='nswe')

    #function to add rounded corners to widget
    def add_background (self,width,height):
        canvas_rounded_corners(self.radius,width,height,self.color,self.can)