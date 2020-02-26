#!/usr/bin/python3
from constants import GPIO,gb_up,gb_down,gb_left,gb_right,time
import time
import random

from constants import time,ButtonMatrix,GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

mainlab = None
currentPos = [0,0]

matrixState = [
            [True,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False],
            [False,False,False,False, False, False, False, False]
          ]

# This are the maps of the labyrinths
Lab1 = [
  [1,2,0,0,0,2,2,2],
  [0,2,0,2,0,2,0,3],
  [0,0,0,2,0,2,0,2],
  [2,2,2,2,0,2,0,2],
  [0,0,0,0,0,2,0,2],
  [2,2,2,2,0,2,0,0],
  [2,0,0,0,0,0,0,2],
  [2,2,2,2,2,2,0,2]
  ]
Lab2 = [
  [0,0,1,2,2,2,2,2],
  [0,2,2,0,2,0,0,0],
  [0,2,0,0,0,0,2,0],
  [0,0,0,0,2,0,2,0],
  [2,0,2,0,2,2,2,2],
  [0,0,2,0,0,0,0,0],
  [2,2,2,2,0,2,2,0],
  [0,0,0,0,0,0,3,0]]
Lab3 = [
  [0,0,0,0,0,0,0,0],
  [0,2,0,2,0,2,2,0],
  [2,2,2,2,0,0,2,0],
  [0,0,1,2,3,0,2,0],
  [0,2,2,2,2,2,2,0],
  [0,2,0,0,0,0,0,0],
  [0,2,0,2,0,2,2,2],
  [0,0,0,2,0,0,0,0]]

def SelectLab(display):
    global mainlab
    choosenindex = random.randint(0,2)
    if(choosenindex == 0):
        mainlab = Lab1
        display.SetImage("assets/lab/1.png")
    elif(choosenindex == 1):
        mainlab = Lab2
        display.SetImage("assets/lab/2.png")
    elif(choosenindex == 2):
        mainlab = Lab3
        display.SetImage("assets/lab/3.png")

def allOff():
    for row in range(len(matrixState)):
        for col in range(len(matrixState[row])):
            if(matrixState[row][col]):
                matrixState[row][col] = False

def Enigme():
    return "Les verts sont vos amis !"

def Title():
    return "Labyrinthe"

def SpawnPoint():
    for row in range(len(mainlab)) :
        for col in range(len(mainlab)) :
            if(mainlab[row][col] == 1):
                currentPos[0] = row
                currentPos[1] = col
                pass

def draw():
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, width=8, height=8)
    with canvas(device) as draw:
        for row in range(len(matrixState)):
            for col in range(len(matrixState[row])):
                if(matrixState[row][col]):
                    draw.rectangle((row,col,row,col),outline="white")

def refreshPosition():
    allOff()
    matrixState[currentPos[0]][currentPos[1]] = True
    draw()
    pass

def IsMoveOk(dir):
    if(dir == "UP"):
        return (currentPos[0] - 1 >= 0 and mainlab[currentPos[0]-1][currentPos[1]] != 2)
    if(dir == "DOWN"):
        return (currentPos[0] + 1 < 8 and mainlab[currentPos[0]+1][currentPos[1]] != 2)
    if(dir == "RIGHT"):
        return (currentPos[1] - 1 >= 0 and mainlab[currentPos[0]][currentPos[1]-1] != 2)
    if(dir == "LEFT"):
        return (currentPos[1] + 1 < 8 and mainlab[currentPos[0]][currentPos[1]+1] != 2)

def IsWin():
    return mainlab[currentPos[0]][currentPos[1]] == 3
    

def moving(dir):
    if(dir == "UP"):
        if(IsMoveOk("UP")):
            currentPos[0] -= 1
        else:
            SpawnPoint()
            
    if(dir == "DOWN"):
        if(IsMoveOk("DOWN")):
            currentPos[0] += 1
        else:
            SpawnPoint()
    
    if(dir == "LEFT"):
        if(IsMoveOk("LEFT")):
            currentPos[1] += 1
        else:
            SpawnPoint()
        
    if(dir == "RIGHT"):
        if(IsMoveOk("RIGHT")):
            currentPos[1] -= 1
        else:
            SpawnPoint()

    refreshPosition()

def Start(display):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gb_up,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_down,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_left,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gb_right,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    SelectLab(display)
    display.Display()
    SpawnPoint()
    
    refreshPosition()
        
    playing = True
        
    oldUp = False
    oldDown = False
    oldLeft = False
    oldRight = False
    
    up = None
    down = None
    left = None
    right = None
    limit = True
    
    while playing:
        oldUp = up
        oldDown = down
        oldLeft = left
        oldRight = right
        
        up = GPIO.input(gb_up) == 0
        down = GPIO.input(gb_down) == 0
        left = GPIO.input(gb_left) == 0
        right = GPIO.input(gb_right) == 0
        
        if(oldUp == False and up):
            moving("UP")
            time.sleep(.1)
        
        if(oldDown == False  and down):
            moving("DOWN")
            time.sleep(.1)
        
        if(oldLeft == False  and left):
            moving("LEFT")
            time.sleep(.1)
        
        if(oldRight == False  and right):
            moving("RIGHT")
            time.sleep(.1)
        
        if(IsWin()):
            playing = False
            print("ENIGME TERMINEE %s" %Title())
            
    display.SetImage("")
    display.Display()
