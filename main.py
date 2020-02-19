#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres

import F2 # Enigme de la lumière
import F3 # Enigme du labyrinthe
import F4 # Enigme humidité
import F5 # Enigme bataille navale
import F6 # Enigme des carrés rouge
import F7 # Code avec les cates RFID
import F9 # Simon says

from window import UI  # Affichage des énigmes sur l'écran du raspberry

def Update_View(userInterface,title, enigmetxt, enigmenb,maxEnigmeNb):
    userInterface.SetTitle(title)
    userInterface.SetEnigmeText(enigmetxt)
    userInterface.SetEnigmeNumberText("Enigme %02d/%02d"%(enigmenb, maxEnigmeNb))
    userInterface.Display()

def Start(userInterface):

    # F9,F2, F3, F4, F5, F6, F7
    Enigmalist = [F2]
    
    index = 0
    while(index < len(Enigmalist)):
        Update_View(userInterface,Enigmalist[index].Title(), Enigmalist[index].Enigme(), index+1,len(Enigmalist))
        Enigmalist[index].Start(userInterface)
        index += 1

    userInterface.Destroy()
        
    
    

