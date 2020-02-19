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
userInterface.SetEnigmeNumberText("")
userInterface.Update_View("CROW'SCAPE GAME", "TO START THE GAME, SCAN THE CARD A")

waitingToPlay = True
card1_id = 109 #A

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
time.sleep(1)
userInterface.Update_View("Beginning in ...", "2")
time.sleep(1)
userInterface.Update_View("Beginning in ...", "1")
time.sleep(1)


# Creating both process
p1 = Process(target=Timer.Start,) # Process the timer
p2 = Process(target=main.Start , args=(userInterface,)) # Process of the game

playing = True

# Beginning the game
p1.start()
p2.start()

endText = "YOU WIN"

while playing:
    
    # Checking if the Process 1 is still alive
    if(p1.is_alive() is False):
        print("THE BOMB EXPLODED")
        playing = False
        endText = "YOU FAIL"
    
    # Checking if the Process 2 is still alive
    if(p2.is_alive() is False):
        print("YOU WIN")
        playing = False


print ('Process1 not terminated:', p1, p1.is_alive())
print ('Process2 not terminated:', p2, p2.is_alive())
p1.terminate()
p2.terminate()
print ('Process1 terminated:', p1, p1.is_alive())
print ('Process2 terminated:', p2, p2.is_alive())
p1.join()
p2.join()
print ('Process1 joined:', p1, p1.is_alive())
print ('Process2 joined:', p2, p2.is_alive())


print("END OF GAME")


#Creating the main menu interface
userInterface.SetEnigmeNumberText("")
userInterface.Display()

endText = "YOU WIN"

if(endText == "YOU WIN"):
    userInterface.SetImage("win.png")
else:
    userInterface.SetImage("lose.png")
    
userInterface.Update_View(endText, "Thanks for playing \n Card B to restart")

waitingToPlay = True
card1_id = 133 #A

# Waiting for the players card to start the game
while waitingToPlay:
    time.sleep(0.1)
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        if uid[2] == card1_id:
            waitingToPlay = False

# Destroying the main menu interface
userInterface.Destroy()
    
