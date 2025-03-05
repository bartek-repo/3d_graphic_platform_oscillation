import tkinter
from tkinter.ttk import Label
from tkinter import font, Entry
from canvas_rounded_corners import *
import  inputText
from inputText import InputText

colors = {"darkerBlue" : "#6DAEC2",
          "lightnessBlue" : "#76C9D5",
          "grey" : "#D9D9D9"}



root = tk.Tk()
root.geometry("500x300")
root.title("Add Objects")
root.configure()

root.columnconfigure((0,1), weight = 1, uniform = 'a')
root.columnconfigure((2,3), weight = 2, uniform = 'a')
root.rowconfigure(0,weight = 2, uniform = 'b')
root.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight = 1, uniform = 'b')

fontContainer = font.Font(family="Times New Roman", size=8, weight="bold")

#containers
topContainer = tk.Canvas(background= colors["grey"],highlightthickness=0)
bottomContainer = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
containerHandle = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
containerOriginTop = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
containerOriginBottom = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
containerMove = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
containerListObjects = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)

topContainer.grid(row = 0, column = 0,columnspan=4,sticky='nsew')
bottomContainer.grid(row = 1, column = 0,columnspan=4,rowspan=11,sticky='nsew')
containerHandle.grid(row = 1, column = 0, rowspan = 3,columnspan=2,padx = 5,pady=5)
containerOriginTop.grid(row = 4, column = 0, rowspan = 3,columnspan=2,padx = 5,pady=5)
containerOriginBottom.grid(row = 7, column = 0, rowspan = 3,columnspan=2,padx = 5,pady=5)
containerMove.grid(row = 1, column = 2,rowspan = 11,padx=5, pady=5)
containerListObjects.grid(row=1, column=3,rowspan=9, padx=5, pady=5)
root.update()

#rounded corners containers
canvas_rounded_corners(8,containerHandle.winfo_width(),containerHandle.winfo_height(),colors["lightnessBlue"], containerHandle)
canvas_rounded_corners(8,containerOriginTop.winfo_width(),containerOriginTop.winfo_height(),colors["lightnessBlue"], containerOriginTop)
canvas_rounded_corners(8,containerOriginBottom.winfo_width(),containerOriginBottom.winfo_height(),colors["lightnessBlue"], containerOriginBottom)
canvas_rounded_corners(8,containerMove.winfo_width(),containerMove.winfo_height(),colors["lightnessBlue"], containerMove)
canvas_rounded_corners(8,containerListObjects.winfo_width(),containerListObjects.winfo_height(),colors["lightnessBlue"], containerListObjects)

#buttons
uploadButton = tk.Canvas(background= colors["grey"],highlightthickness=0)
textUploadButton = Label(text="upload",font=font.Font(family="Times New Roman", size=8, weight="bold"),background=colors["darkerBlue"],foreground='white')
buttonPath = tk.Canvas(background= colors["grey"],highlightthickness=0)
textButtonPath = Label(text="Path",font=font.Font(family="Times New Roman", size=8, weight="bold"),background=colors["darkerBlue"],foreground='white')
buttonAdd = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
textButtonAdd = Label(text="add",font=font.Font(family="Times New Roman", size=16, weight="bold"),background=colors["lightnessBlue"],foreground='white')
buttonRemove = tk.Canvas(background= colors["darkerBlue"],highlightthickness=0)
textButtonRemove = Label(text="remove",font=font.Font(family="Times New Roman", size=16, weight="bold"),background=colors["lightnessBlue"],foreground='white')



#position of buttons
uploadButton.grid(row=0,column=0,padx=10,pady=10)
textUploadButton.grid(row=0,column=0)
buttonPath.grid(row=0,column=1,padx=10,pady=10)
textButtonPath.grid(row=0,column=1)
buttonAdd.grid(row=10,column=0,rowspan = 2,columnspan = 2,padx=5,pady=5,sticky='nswe')
textButtonAdd.grid(row=10, column=0, rowspan=2, columnspan=2)
buttonRemove.grid(row=10, column=3, rowspan=2, padx=5, pady=5, sticky='nswe')
textButtonRemove.grid(row=10, column=3, rowspan=2)



#rounded corners buttons
root.update()
canvas_rounded_corners(8,uploadButton.winfo_width(),uploadButton.winfo_height(),colors["darkerBlue"], uploadButton)
canvas_rounded_corners(8,buttonPath.winfo_width(),buttonPath.winfo_height(),colors["darkerBlue"], buttonPath)
canvas_rounded_corners(8,buttonAdd.winfo_width(),buttonAdd.winfo_height(),colors["lightnessBlue"], buttonAdd)
canvas_rounded_corners(8,buttonRemove.winfo_width(),buttonRemove.winfo_height(),colors["lightnessBlue"], buttonRemove)

#inputtext
inputPath = Entry(root,highlightthickness=0,borderwidth=0)
containerInputPath = tkinter.Canvas(background= colors["grey"],highlightthickness=0)

framex = tkinter.Frame(root)
framex.grid(row=3,column=2,padx=5)
framex.grid_rowconfigure(0,weight=1)
framex.grid_columnconfigure(0,weight=1)
canvaaa = tkinter.Canvas(framex,bg='pink')
canvaaa.grid(row=0,column=0)

inputSelectHandle = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputSelectTopOrigin = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputSelectBottomOrigin = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)

#inputMove1 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputMove2 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputMove3 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputMove4 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputMove5 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)
inputMove6 = InputText(root,fontContainer,color='white',backgroundcolor=colors["lightnessBlue"],fontcolor='black',radius=10)

#inputtext grid
containerInputPath.grid(row=0,column=2,columnspan=2,pady=10,padx=10, sticky='nswe')
inputPath.grid(row=0,column=2,columnspan=2,pady=15,padx=20, sticky='nswe')
inputPath.lift()
inputSelectHandle.grid(row=2,column=0,columnspan=2,rowspan=2,pady=15)
inputSelectTopOrigin.grid(row=5,column=0,columnspan=2,rowspan=2,padx=20,pady=15,sticky='nswe')
inputSelectBottomOrigin.grid(row=8,column=0,columnspan=2,rowspan=2,padx=20,pady=15,sticky='nswe')


#inputMove1.grid(row=3,column=2,padx=40,pady=5,sticky='nswe')
#inputMove2.grid(row=0,column=0,sticky='nsew')
inputMove3.grid(row=5,column=2,padx=40,pady=5,sticky='nswe')
inputMove4.grid(row=6,column=2,padx=40,pady=5,sticky='nswe')
inputMove5.grid(row=7,column=2,padx=40,pady=5,sticky='nswe')
inputMove6.grid(row=8,column=2,padx=40,pady=5,sticky='nswe')


#rounded corners inputText
root.update()
canvas_rounded_corners(4,containerInputPath.winfo_width(),containerInputPath.winfo_height(),"white", containerInputPath)
inputSelectHandle.add_background(width=inputSelectHandle.winfo_width(),height=inputSelectHandle.winfo_height())
inputSelectTopOrigin.add_background(width=inputSelectTopOrigin.winfo_width(),height=inputSelectTopOrigin.winfo_height())
inputSelectBottomOrigin.add_background(width=inputSelectBottomOrigin.winfo_width(),height=inputSelectBottomOrigin.winfo_height())
#inputMove1.add_background(width=inputMove1.winfo_width(),height=inputMove1.winfo_height())
inputMove2.add_background(width=inputMove2.winfo_width(),height=inputMove2.winfo_height())
inputMove3.add_background(width=inputMove3.winfo_width(),height=inputMove3.winfo_height())
inputMove4.add_background(width=inputMove4.winfo_width(),height=inputMove4.winfo_height())
inputMove5.add_background(width=inputMove5.winfo_width(),height=inputMove5.winfo_height())
inputMove6.add_background(width=inputMove6.winfo_width(),height=inputMove6.winfo_height())





#events buttons
uploadButton.bind("<ButtonRelease-1>",lambda event: print("Upload"))
textUploadButton.bind("<ButtonRelease-1>",lambda event: print("Upload"))

buttonPath.bind("<ButtonRelease-1>", lambda event: print("path")  )
textButtonPath.bind("<ButtonRelease-1>",lambda event: print("path") )

def upload_button_motion (e):
    uploadButton.config(cursor="hand2")
    textUploadButton.config( cursor="hand2")

def upload_button_leave(e):
    uploadButton.config(background=colors["darkerBlue"],cursor="arrow")
    textUploadButton.config(cursor="arrow")

def path_button_motion (e):
    buttonPath.config(background=colors["grey"],cursor="hand2")
    textButtonPath.config( cursor="hand2")
def path_button_leave(e):
    buttonPath.config(background=colors["darkerBlue"],cursor="arrow")
    textButtonPath.config(cursor="arrow")

uploadButton.bind("<Motion>", upload_button_motion  )
textUploadButton.bind("<Motion>",upload_button_motion )

uploadButton.bind("<Leave>",upload_button_leave )
textUploadButton.bind("<Leave>",upload_button_leave )

buttonPath.bind("<Motion>", path_button_motion  )
textButtonPath.bind("<Motion>", path_button_motion  )

buttonPath.bind("<Leave>",path_button_leave)
textButtonPath.bind("<Leave>",path_button_leave)






root.mainloop()


