#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time
import random
alea = ['^','v','<','>']
SUITE_SIZE = 5

def Title():
    return "Simon dis ..."
def Enigme():
    return ""

def Start(display):
    suite = []
    for i in range(SUITE_SIZE):
        suite.append(random.choice(alea))

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gb_up,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_down,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_left,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_right,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    
    indexPlaying = 0
    while indexPlaying < len(suite):
        
        ShowSuite(indexPlaying+1,suite,display)
        waitingInput = True
        actualInput = 0
        
        oldUp = False
        oldDown = False
        oldLeft = False
        oldRight = False
        
        up = None
        down = None
        left = None
        right = None
    
        while waitingInput:
            oldUp = up
            oldDown = down
            oldLeft = left
            oldRight = right
        
            up = GPIO.input(gb_up) != 1
            down = GPIO.input(gb_down) != 1
            left = GPIO.input(gb_left) != 1
            right = GPIO.input(gb_right) != 1

            if((not oldUp and up) or (not oldDown and down) or (not oldLeft and left) or (not oldRight and right)):
                correctInput = False
                if(suite[actualInput] == '^' and up):
                    correctInput = True
                elif(suite[actualInput] == '<' and left): 
                    correctInput = True
                elif(suite[actualInput] == '>' and right): 
                    correctInput = True
                elif(suite[actualInput] == 'v' and down):
                    correctInput = True
                if(correctInput):
                    print("Ok")
                    if(indexPlaying == actualInput):
                        waitingInput = False
                        indexPlaying += 1
                    actualInput += 1
                else:
                    actualInput = 0
                    waitingInput = False
                    
    
def ShowSuite(to,suite,display):
    display.SetEnigmeText("")
    for i in range(to):
        PrintI(suite[i],display)
    display.SetEnigmeText("Your turn...")
    display.Display()
                
def PrintI(i,display):
    print(i)
    if(i == '^'):
        display.SetImage("assets/simon/up.png")
    elif(i == '<'): 
        display.SetImage("assets/simon/left.png")
    elif(i == '>'): 
        display.SetImage("assets/simon/right.png")
    elif(i == 'v'):
        display.SetImage("assets/simon/down.png")
    display.Display()
    time.sleep(1)
    display.SetImage()
    display.Display()
    time.sleep(.5)
