#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time
import time

from constants import time,ButtonMatrix,GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


currentPos = [3,3]
matrixState = []

def allOff():
    global matrixState

    matrixState = [
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False],
                [False,False,False,False, False, False, False, False]
              ]

def Enigme():
    return "Les verts sont vos amis !"

def Title():
    return "Labyrinthe"

def draw():
    global matrixState
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, width=8, height=8)
    with canvas(device) as draw:
        for row in range(len(matrixState)):
            for col in range(len(matrixState[row])):
                if(matrixState[row][col]):
                    draw.rectangle((row,col,row,col),outline="white")

def refreshPosition():
    global matrixState
    allOff()
    matrixState[currentPos[0]][currentPos[1]] = True
    draw()
    pass

def Start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gb_up,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_down,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_left,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_right,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    refreshPosition()
        
    playing = True
        
    while playing:
        up = GPIO.input(gb_up) == 0
        down = GPIO.input(gb_down) == 0
        left = GPIO.input(gb_left) == 0 
        right = GPIO.input(gb_right) == 0
        #print("%d %d %d %d" % (up,down,left,right)) 
        if up:
            print("haut")
            pass

        if down:
            print("bas")
            pass

        if left:
            print("gauche")
            pass

        if right:
            print("droite")
            pass

        refreshPosition()
        
            
            