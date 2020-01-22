#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time
import random
alea = ['^','v','<','>']
SUITE_SIZE = 5

def Enigme():
    return "Simon dis ..."

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
        
        while waitingInput:
            up = GPIO.input(gb_up)
            down = GPIO.input(gb_down)
            left = GPIO.input(gb_left)
            right = GPIO.input(gb_right)

            if(up or down or left or right):
                correctInput = False
                waitingInput = False

                if(suite[indexPlaying] == '^' and up):
                    correctInput = True
                elif(suite[indexPlaying] == '<' and left): 
                    correctInput = True
                elif(suite[indexPlaying] == '>' and right): 
                    correctInput = True
                elif(suite[indexPlaying] == 'v' and down):
                    correctInput = True
                if(correctInput):
                    indexPlaying+=1
    
def ShowSuite(to,suite,display):
    for i in range(to):
        PrintI(suite[i],display)
    display.SetImage('Simon_None.png')
                
def PrintI(i,display):
    if(i == '^'):
        display.SetImage('Simon_Up.png')
    elif(i == '<'): 
        display.SetImage('Simon_Left.png')
    elif(i == '>'): 
        display.SetImage('Simon_Right.png')
    elif(i == 'v'):
        display.SetImage('Simon_Down.png')
    time.sleep(1)
