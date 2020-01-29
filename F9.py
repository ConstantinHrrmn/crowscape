#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time
import time

suite = ['^','v','<','>']

def Enigme():
    return "Simon dis ..."

def Start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gb_up,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_down,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_left,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_right,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    
    print("Bon bah ca ce lance")
    indexPlaying = 0
    while indexPlaying < len(suite):
        ShowSuite(indexPlaying+1)
        waitingInput = True
        while waitingInput:
            up = GPIO.input(gb_up) == 0
            down = GPIO.input(gb_down) == 0
            left = GPIO.input(gb_left) == 0 
            right = GPIO.input(gb_right) == 0
             #print("%d %d %d %d" % (up,down,left,right)) 
            
            if(up or down or left or right):
                waitingInput = False
        
        indexPlaying+=1
    
def ShowSuite(to):
    for i in range(to):
        PrintI(suite[i])
                
def PrintI(i):
    print(i)
    time.sleep(1)
