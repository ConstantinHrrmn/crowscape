#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageTk

class UI:
    
    
    def __init__(self):
        self.mainview = Tk(className='CrowScape')
        self.mainview.attributes("-fullscreen", True)   
        
        self.titleLabel = Label(self.mainview, text="Enigme 1", font=("Arial", 64))
        self.enigmeLabel = Label(self.mainview, text="Indice pour enigme", font=("Arial", 35))
        self.enigmeNumberLabel = Label(self.mainview, text="Numéro Enigme", font=("Arial", 32))
        self.lblImage = Label()

    def SetTitle(self, textLabel):
        self.titleLabel.config(text=textLabel)
    
    def SetEnigmeNumberText(self, textLabel):
        self.enigmeNumberLabel.config(text=textLabel)

    def SetEnigmeText(self, textLabel):
        self.enigmeLabel.config(text=textLabel)

    def PlaceAllLabels(self):
        self.titleLabel.place(relx=.5, rely=.1, anchor="center")
        self.enigmeLabel.place(relx=.5, rely=.3, anchor="center")
        self.enigmeNumberLabel.place(relx=0.0, rely=1.0, anchor='sw')
    
    def Display(self, interval=100):
        self.PlaceAllLabels()
        self.mainview.after(interval,self.mainview.quit)
        self.mainview.mainloop()
        
    def Destroy(self, interval = 1):
        self.mainview.after(interval,self.mainview.destroy)
        
    def Update_View(self, title, enigmetxt):
        self.SetTitle(title)
        self.SetEnigmeText(enigmetxt)
        self.Display()
    
    def SetImage(self, imageName=""):
        if imageName != "":
            
            render = ImageTk.PhotoImage(master=self.mainview,file=imageName) # Create a render of the enigme image
        
            self.lblImage.after(100, self.lblImage.destroy)
            self.lblImage = Label(self.mainview, image=render)
            self.lblImage.image = render
            self.lblImage.place(relx=.5, rely=.65, anchor="center")
            pass
        else:
            if(self.lblImage is not None):
                self.lblImage.destroy()
            pass
