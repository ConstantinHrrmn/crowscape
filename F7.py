#!/usr/bin/python3

# -*- coding: utf8 -*-
# Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
import RPi.GPIO as GPIO
import MFRC522
import signal
import time

GPIO.setwarnings(False)


#signal.signal(signal.SIGINT, end_read)
# create the reader object
MIFAREReader = MFRC522.MFRC522()

def Enigme():
    return "il n'y as pas encore d'énigme"

def Step():
    global index 
    return index

def Start():
    continue_reading = True
    continue_enigme = True
    global index
    
    card1_id = 204
    card2_id = 59
    
    cardids = [card1_id, card2_id, card1_id, card1_id]
    
    while continue_enigme:
        
        index += 1
        continue_reading = True
        
        if index >= len(cardids):
            continue_enigme = False
        else:
            print("POSEZ")

            while continue_reading:
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                if status == MIFAREReader.MI_OK:
                    print("Carte détectée")

                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                if status == MIFAREReader.MI_OK:      
                    if cardids[index] == uid[0]:
                        print("CARTE OK")
                        continue_reading = False
                    else:
                        print("ERROR L'ENIGME VA RECOMMENCER...")
                        continue_reading = False
                        index = -1      
                                        
            print("LEVEZ")
            time.sleep(3)
      
index = -1
Start()