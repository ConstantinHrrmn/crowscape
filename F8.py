#!/usr/bin/python3
from tkinter import *
from PIL import *

class UI:
    
    
    def __init__(self):
        self.mainview = Tk(className='CrowScape')
        self.mainview.geometry("{0}x{1}+0+0".format(self.mainview.winfo_screenwidth(), self.mainview.winfo_screenheight()))    
        
        self.titleLabel = Label(self.mainview, text="Enigme 1", font=("Arial", 64))
        self.enigmeLabel = Label(self.mainview, text="Indice pour enigme", font=("Arial", 48))
        self.enigmeNumberLabel = Label(self.mainview, text="Numéro Enigme", font=("Arial", 32))

    def SetTitle(self, textLabel):
        self.titleLabel.config(text=textLabel)
    
    def SetEnigmeNumberText(self, textLabel):
        self.enigmeNumberLabel.config(text=textLabel)

    def SetEnigmeText(self, textLabel):
        self.enigmeLabel.config(text=textLabel)

    def PlaceAllLabels(self):
        self.titleLabel.place(relx=.5, rely=.10, anchor="center")
        self.enigmeLabel.place(relx=.5, rely=.20, anchor="center")
        self.enigmeNumberLabel.place(relx=0.0, rely=1.0, anchor='sw')
    
    def Display(self):
        self.PlaceAllLabels()
        self.mainview.mainloop()
    


"""userInterface = UI()

userInterface.SetTitle("eowrzqw")
userInterface.SetEnigmeText("")
userInterface.SetEnigmeNumberText("Enigme XX/XX")

userInterface.Display()"""





"""photo = PhotoImage(file="giphy.gif")
w = Label(mainview, image=photo)
w.pack()

title.set("Test")
enigmeText.set("Enigme Test")
enigmeNumberText.set("Enigme XX/XX")

mainview.mainloop()"""