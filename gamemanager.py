#!/usr/bin/python3

from multiprocessing import Process

from window import UI  # Affichage des énigmes sur l'écran du raspberry

import Timer
import RPi.GPIO as GPIO

import MFRC522
import main
import time

# create the reader object
MIFAREReader = MFRC522.MFRC522()
    

#Creating the main menu interface
userInterface = UI()
userInterface.Initlabels()
userInterface.SetEnigmeNumberText("")
userInterface.Update_View("CROW'SCAPE GAME", "TO START THE GAME, SCAN THE CARD A")

waitingToPlay = True
card1_id = 109 #The card A

# Waiting for the players card to start the game
while waitingToPlay:
    time.sleep(0.1)
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        if uid[2] == card1_id:
            waitingToPlay = False

# Timer before beginning of the game
userInterface.Update_View("Beginning in ...", "3")
time.sleep(1) # 1 second sleep
userInterface.Update_View("Beginning in ...", "2")
time.sleep(1) # 1 second sleep
userInterface.Update_View("Beginning in ...", "1")
time.sleep(1) # 1 second sleep

# Creating both process
p1 = Process(target=Timer.Start,) # Process the timer
p2 = Process(target=main.Start ,) # Process of the game  args=(userInterface,)

playing = True

#Starting the timer
p1.start()
#Starting the game
p2.start()

while playing:
    # Checking if the Process 1 is still alive
    if(p1.is_alive() is False):
        print("THE BOMB EXPLODED")
        playing = False
    
    # Checking if the Process 2 is still alive
    if(p2.is_alive() is False):
        print("YOU WIN")
        playing = False

p1.terminate()
p2.terminate()
p1.join()
p2.join()

print("END OF GAME")

    
