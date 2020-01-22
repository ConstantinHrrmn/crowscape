#!/usr/bin/python3

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import random

GPIO.setwarnings(False)

index = -1
enigme = ""

# create the reader object
MIFAREReader = MFRC522.MFRC522()

def Enigme():
    return enigme
    
def Title():
    return "Right sequence"

def Step():
    global index 
    return index

def RandomSequence(seq_len):
    global enigme 
    card1_id = 204
    card2_id = 59
    card3_id = 105
    
    last_id = 0
    cards = []
    
    for i in range(seq_len):
        sel = random.choice([card1_id,card2_id,card3_id])
        while(sel == last_id):
            sel = random.choice([card1_id,card2_id,card3_id])
        last_id = sel
        cards.append(sel)
    
    for x in cards:
        if x == card1_id:
            enigme += "B"
        elif x == card2_id:
            enigme += "G"
        elif x == card3_id:
            enigme += "R"
        #enigme += " "
    
    return cards
        

def Start(display):
    continue_reading = True
    continue_enigme = True
    global index
    global cards
    global enigme
    
    cardids = cards
    enigmebackup = enigme
    
    last = 0
    while continue_enigme:
        
        index += 1
        continue_reading = True
        
        if index >= len(cardids):
            continue_enigme = False
        else:
            while continue_reading:
                time.sleep(0.1)
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                
                (status,uid) = MIFAREReader.MFRC522_Anticoll()
                if status == MIFAREReader.MI_OK:
                    if uid[0] != last:      
                        if cardids[index] == uid[0]:
                        
                            s = list(enigme)
                            s[index] = '-'
                            enigme = "".join(s)
                            display.SetEnigmeText(enigme)
                            display.Display()
                            
                            print("CARTE OK %s" %enigme)
                            continue_reading = False
                            last = uid[0]
                        else:
                            print("ERROR L'ENIGME VA RECOMMENCER...")
                            continue_reading = False
                            index = -1    
                            last = 0
                            enigme = enigmebackup
                            display.SetEnigmeText(enigme)
                            display.Display()
    
    print ("ENIGME TERMINEE")


cards = RandomSequence(10)
