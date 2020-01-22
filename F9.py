#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time

suite = ['^','v','<','>']


def Enigme():
    return "Simon dis ..."

def Start():
    GPIO.setup(gb_up,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_down,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_left,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gb_right,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    
    
    print("Bon bah ca ce lance")
    indexPlaying = 0
    while indexPlaying < len(suite):
        ShowSuite(indexPlaying+1)
        waitingInput = True
        while waitingInput:
            time.sleep(0.1)
            up = GPIO.input(gb_up)
            down = GPIO.input(gb_down)
            left = GPIO.input(gb_left)
            right = GPIO.input(gb_right)
            
            if(up or down or left or right):
                print("up = "+str(up))
                print("down = "+str(down))
                print("left = "+str(left))
                print("right = "+str(right))
                waitingInput = False
        
        indexPlaying+=1
    
def ShowSuite(to):
    for i in range(to):
        PrintI(suite[i])
                
def PrintI(i):
    print(i)
    time.sleep(1)
    
Start()