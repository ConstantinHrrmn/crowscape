#!/usr/bin/python3
from constants import time,ButtonMatrix,GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

buttons = ButtonMatrix()
matrixState = [[False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False]]
#verify that all matrix is good
def allOn():
    for row in matrixState:
        for col in row:
            if(not col):
                return False
    return True

def allOff():
    matrixState = [[False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False]]
    draw()

def Enigme():
    return "Tout dois être rouge !"

def draw():
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, width=8, height=8)
    with canvas(device) as draw:
        for row in range(len(matrixState)):
            for col in range(len(matrixState[row])):
                if(matrixState[row][col]):
                    draw.rectangle((row*2,col*2,row*2+1,col*2+1),outline="white")

def Start(cascaded, block_orientation, rotate):
    draw()
    playing = True
    while(playing):
                for j in range(len(buttons.columnPins)):
                    # set each output pin to low
                    GPIO.output(buttons.columnPins[j],0)
                    for i in range(len(buttons.rowPins)):
                        if GPIO.input(buttons.rowPins[i]) == 0:
                            # button pressed, activate it
                            buttons.activateButton(i,j)

                            matrixState[i][j] = not matrixState[i][j]
                            if(i-1 >= 0):
                                matrixState[i-1][j] = not matrixState[i-1][j]
                            if(i+1 < len(matrixState)):
                                matrixState[i+1][j] = not matrixState[i+1][j]
                            if(j-1 >= 0):
                                matrixState[i][j-1] = not matrixState[i][j-1]
                            if(j+1 < len(matrixState[i])):
                                matrixState[i][j+1] = not matrixState[i][j+1]
                            draw()
                            
                            if(allOn()):
                                playing = False


                            while(buttons.buttonHeldDown(i)):
                                pass
                    # return each output pin to high
                    GPIO.output(buttons.columnPins[j],1)
    print("You successfully completed the module")


# if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
 #   try:
 #      Start(cascaded=1, block_orientation=90, rotate=0)
  #  except KeyboardInterrupt:
    #    pass
