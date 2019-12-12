#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres 

import F2 # Enigme de la lumière
import F4 # Enigme humidité
import F5 # Enigme bataille navale
import F6 # Enigme des carrés rouge

def Start():
    print(F2.Enigme())
    F2.Start()
    
    print(F5.Enigme())
    F5.Start()
    
    print(F6.Enigme())
    F6.Start(cascaded=1, block_orientation=90, rotate=0)
    
    print(F4.Enigme())
    F4.Satart()
    