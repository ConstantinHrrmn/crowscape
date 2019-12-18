#!/usr/bin/python3
from tkinter import *
from PIL import *

mainview = Tk(className='CrowScape')
#Force the window size at screen size
mainview.geometry("{0}x{1}+0+0".format(mainview.winfo_screenwidth(), mainview.winfo_screenheight()))

title = StringVar()
enigmeText = StringVar()
enigmeNumberText = StringVar()

titleLabel = Label(mainview, textvariable=title, font=("Arial", 64))
titleLabel.pack()

enigmeLabel = Label(mainview, textvariable=enigmeText, font=("Arial", 48))
enigmeLabel.pack()

enigmeNumber = Label(mainview, textvariable=enigmeNumberText, font=("Arial", 32))
enigmeNumber.place(relx=0.0, rely=1.0, anchor='sw')

photo = PhotoImage(file="giphy.gif")
w = Label(mainview, image=photo)
w.photo = photo
w.pack()

title.set("Test")
enigmeText.set("Enigme Test")
enigmeNumberText.set("Enigme XX/XX")

mainview.mainloop()