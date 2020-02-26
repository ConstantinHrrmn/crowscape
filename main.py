#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres

import enigmes.F2 # Enigme de la lumière
import enigmes.F3 # Enigme du labyrinthe
import enigmes.F4 # Enigme humidité
import enigmes.F5 # Enigme bataille navale
import enigmes.F6 # Enigme des carrés rouge
import enigmes.F7 # Code avec les cates RFID
import enigmes.F9 # Simon says
import random

from window import UI  # Affichage des énigmes sur l'écran du raspberry

def Update_View(ui,title, enigmetxt, enigmenb,maxEnigmeNb):
    ui.SetTitle(title)
    ui.SetEnigmeText(enigmetxt)
    ui.SetEnigmeNumberText("Enigme %02d/%02d"%(enigmenb, maxEnigmeNb))
    ui.Display()

def Start(): #userInterface

    # Création de l'interface
    ui = UI()
    ui.Initlabels()
    ui.SetEnigmeNumberText("")
    ui.Update_View("", "")

    # F9,F2, F3, F4, F5, F6, F7
    Enigmalist = [enigmes.F9, enigmes.F2, enigmes.F3, enigmes.F4, enigmes.F5, enigmes.F6, enigmes.F7]
    #Shuffle alle the enigmes
    random.shuffle(Enigmalist)

    index = 0
    while(index < len(Enigmalist)):
        Update_View(ui,Enigmalist[index].Title(), Enigmalist[index].Enigme(), index+1,len(Enigmalist))
        Enigmalist[index].Start(ui)
        index += 1

    # Suppression de l'interface
    ui.quit()
        
    
    

