#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres

import F2 # Enigme de la lumière
import F4 # Enigme humidité
import F5 # Enigme bataille navale
import F6 # Enigme des carrés rouge
import F7 # Code avec les cates RFID
import F9 # Simon says

from window import UI  # Affichage des énigmes sur l'écran du raspberry

userInterface = UI()
userInterface.Display()

Enigmalist = [F7]

def Update_View(title, enigmetxt, enigmenb):
    userInterface.SetTitle(title)
    userInterface.SetEnigmeText(enigmetxt)
    userInterface.SetEnigmeNumberText("Enigme %02d/%02d"%(enigmenb, len(Enigmalist)))
    userInterface.Display()

def Start():
    index = 0
    while(index < len(Enigmalist)):
        Update_View(Enigmalist[index].Title(), Enigmalist[index].Enigme(), index+1)
        Enigmalist[index].Start(userInterface)
        index += 1
    
    

