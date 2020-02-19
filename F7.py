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
    return "La bonne séquence"

def Step():
    global index 
    return index

def RandomSequence(seq_len):
    global enigme 
    card1_id = 109 #A
    card2_id = 133 #B
    card3_id = 220 #C
    card4_id = 107 #D
    card5_id = 131 #E
    card6_id = 239 #F
    card7_id = 237 #G
    
    
    last_id = 0
    cards = []
    
    for i in range(seq_len):
        sel = random.choice([card1_id,card2_id,card3_id,card4_id,card5_id,card6_id,card7_id])
        while(sel == last_id):
            sel = random.choice([card1_id,card2_id,card3_id,card4_id,card5_id,card6_id,card7_id])
        last_id = sel
        cards.append(sel)
    
    for x in cards:
        if x == card1_id:
            enigme += "A"
        elif x == card2_id:
            enigme += "B"
        elif x == card3_id:
            enigme += "C"
        elif x == card4_id:
            enigme += "D"
        elif x == card5_id:
            enigme += "E"
        elif x == card6_id:
            enigme += "F"
        elif x == card7_id:
            enigme += "G"
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
                    print(uid[2]);
                    if uid[2] != last:
                        if cardids[index] == uid[2]:
                        
                            s = list(enigme)
                            s[index] = '-'
                            enigme = "".join(s)
                            display.SetEnigmeText(enigme)
                            display.Display()
                            
                            print("CARTE OK %s" %enigme)
                            continue_reading = False
                            last = uid[2]
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
