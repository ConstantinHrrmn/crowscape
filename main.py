#!/usr/bin/python3

# Script principal qui va gérer toutes les énigmes les unes après les autres 

from htmlmanager import HTMLWriter

import F2 # Enigme de la lumière
import F4 # Enigme humidité
import F5 # Enigme bataille navale
import F6 # Enigme des carrés rouge

def Start():
    F6.allOff()
    
    html = HTMLWriter()
    html.write_html("HELLO", "TEST OK")
    html.create_tab()

    #print(F2.Enigme())
    #F2.Start()
    
    print("Enigme 1 : " + F5.Enigme())
    html.write_html("ENIGME 1", F5.Enigme())
    html.create_tab()
    F5.Start()
    
    print("Enigme 2 : " + F6.Enigme())
    html.write_html("ENIGME 2", F6.Enigme())
    html.create_tab()
    F6.Start(cascaded=1, block_orientation=90, rotate=0)
    
    print(F4.Enigme())
    F4.Start()
    