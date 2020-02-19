#!/usr/bin/python3

from window import UI 

def Start(text):
    userInterface = UI()
    userInterface.Initlabels()
    userInterface.SetEnigmeNumberText("")
    userInterface.Update_View("HELLO", text)
