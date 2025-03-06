import tkinter as tk
from tkinter import font

colors = {"darkerBlue" : "#6DAEC2",
          "lightnessBlue" : "#76C9D5",
          "grey" : "#D9D9D9",
          "white" : "#FFFFFF"}

root = tk.Tk()
root.geometry("1000x500")

fonts = {"buttonTopContainer" : font.Font(family="Times New Roman,Bold",size=15),
         "bottomContainerTitle": font.Font(family="Times New Roman,Bold",size=15),
         "bottomButtonFont": font.Font(family="Times New Roman,Bold",size=20)}

root.rowconfigure(0, weight=2,uniform='a')
root.rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12,13),weight=1,uniform='a')
root.columnconfigure((0,1,2,3,4,5),weight=1,uniform='b')

#containers

containerTop = tk.Canvas(root, bg=colors["grey"],highlightthickness=0)
containerTop.grid(row=0,column=0,columnspan=6,sticky='nswe')

containerButtonUpload = tk.Canvas(root,bg=colors["darkerBlue"],highlightthickness=0)
containerButtonUpload.grid(row=0,column=0,padx=10,pady=10,sticky='nswe')

containerButtonPath = tk.Canvas(root,bg=colors["darkerBlue"],highlightthickness=0)
containerButtonPath.grid(row=0,column=1,padx=10,pady=10,sticky='nswe')

containerInputPath = tk.Canvas(root,bg=colors["white"],highlightthickness=0)
containerInputPath.grid(row=0,column=2,columnspan=4,padx=10,pady=10,sticky='nswe')

containerBottom = tk.Canvas(root, bg=colors["darkerBlue"], highlightthickness=0)
containerBottom.grid(row=1,column=0,rowspan=13,columnspan=6,sticky='nswe')

containerSelectHandle = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerSelectHandle.grid(row=1,column=0,rowspan=3,columnspan=2,
                           padx=5,pady=5,sticky='nswe')
containerSelectTopOrigin = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerSelectTopOrigin.grid(row=4,column=0,rowspan=3,columnspan=2,
                           padx=5,pady=5,sticky='nswe')
containerSelectBottomOrigin = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerSelectBottomOrigin.grid(row=7,column=0,rowspan=3,columnspan=2,
                           padx=5,pady=5,sticky='nswe')
containerButtonAdd = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerButtonAdd.grid(row=10,column=0,rowspan=4,columnspan=2,
                           padx=5,pady=5,sticky='nswe')

containerMoveHandle = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerMoveHandle.grid(row=1,column=2,rowspan=13,columnspan=2,
                           padx=5,pady=5,sticky='nswe')
containerAddedHandle = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerAddedHandle.grid(row=1,column=4,rowspan=9,columnspan=2,
                           padx=5,pady=5,sticky='nswe')

containerButtonRemove = tk.Canvas(root,bg=colors["lightnessBlue"],highlightthickness=0)
containerButtonRemove.grid(row=10,column=4,rowspan=4,columnspan=2,
                           padx=5,pady=5,sticky='nswe')

#labels

labelButtonUpload = tk.Label(root,text="upload",font=fonts["buttonTopContainer"],foreground="white",bg=colors["darkerBlue"])
labelButtonUpload.grid(row=0,column=0)
labelButtonPath = tk.Label(root,text="path",font=fonts["buttonTopContainer"],foreground="white",bg=colors["darkerBlue"])
labelButtonPath.grid(row=0,column=1)

labelContainerSelectHandle = tk.Label(root,text="select handle",font=fonts["bottomContainerTitle"],foreground="white",bg=colors["lightnessBlue"])
labelContainerSelectHandle.grid(row=1,column=0,rowspan=2,columnspan=2,padx=15,pady=15,sticky='nw')
labelContainerSelectTopOrigin = tk.Label(root,text="select top origin",font=fonts["bottomContainerTitle"],foreground="white",bg=colors["lightnessBlue"])
labelContainerSelectTopOrigin.grid(row=4,column=0,rowspan=2,columnspan=2,padx=15,pady=15,sticky='nw')
labelContainerSelectBottomOrigin = tk.Label(root,text="select bottom origin",font=fonts["bottomContainerTitle"],foreground="white",bg=colors["lightnessBlue"])
labelContainerSelectBottomOrigin.grid(row=7,column=0,rowspan=2,columnspan=2,padx=15,pady=15,sticky='nw')
labelContainerMoveHandle = tk.Label(root,text="move handle",font=fonts["bottomContainerTitle"],foreground="white",bg=colors["lightnessBlue"])
labelContainerMoveHandle.grid(row=1,column=2,rowspan=2,columnspan=2,padx=15,pady=15,sticky='nw')
labelContainerListAddedObjects = tk.Label(root,text="added objects",font=fonts["bottomContainerTitle"],foreground="white",bg=colors["lightnessBlue"])
labelContainerListAddedObjects.grid(row=1,column=4,rowspan=2,columnspan=2,padx=15,pady=15,sticky='nw')

labelButtonButtonAdd = tk.Label(root,text="add",font=fonts["bottomButtonFont"],foreground="white",bg=colors["lightnessBlue"])
labelButtonButtonAdd.grid(row=10,column=0,rowspan=4,columnspan=2,padx=15,pady=15)
labelButtonButtonRemove = tk.Label(root,text="remove",font=fonts["bottomButtonFont"],foreground="white",bg=colors["lightnessBlue"])
labelButtonButtonRemove.grid(row=10,column=4,columnspan=2,rowspan=4,padx=15,pady=15)


root.mainloop()