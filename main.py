#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres

import F2 # Enigme de la lumière
import F4 # Enigme humidité
import F5 # Enigme bataille navale
import F6 # Enigme des carrés rouge
import F7 # Code avec les cates RFID

def Start():
    F6.allOff()

    #print(F2.Enigme())
    #F2.Start()

    print("Enigme 1 : " + F5.Enigme())
    F5.Start()

    print("Enigme 2 : " + F6.Enigme())
    F6.Start()

    print("Enigme TAMER : " + F4.Enigme())
    F4.Start()