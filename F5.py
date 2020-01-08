#!/usr/bin/python3

import time
import threading

from constants import lcd, ButtonMatrix, GPIO
from random import seed, randint

# import Timer

my_coords = []

class Coordonnees():
    def __init__(self,row, col):
        self.row = row
        self.col = col

    def GetPos(self):
        val = 'A' if self.row == 3 else 'B' if self.row == 2 else 'C' if self.row == 1 else 'D'
        return val + str(self.col)

def CreateCode():
    for i in range(5):
        row = randint(0,3)
        col = randint(0,3)
        #print("x : " + str(row) + " | y : " + str(col))
        my_coords.append(Coordonnees(row, col))

def Enigme():
    return "Explosez les bateaux aux bonnes coordonnées"

def Start():
    index = 0

    buttons = ButtonMatrix()

    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 16
    lcd_rows = 2

    # Turn backlight on
    lcd.set_backlight(0)

    coordToFound = Coordonnees(0,0)

    CreateCode()
    code = ""
    for co in my_coords:
        code += co.GetPos()
    # Print a two line message
    lcd.message(code)

    coordToFound = my_coords[index]

    module_done = True

    while module_done:
                for j in range(len(buttons.columnPins)):
                    # set each output pin to low
                    GPIO.output(buttons.columnPins[j],0)
                    for i in range(len(buttons.rowPins)):
                        if GPIO.input(buttons.rowPins[i]) == 0:
                            # button pressed, activate it
                            buttons.activateButton(i,j)
                            #print("x:" + str(j) + " | y: " + str(i))

                            if(coordToFound.row == j and coordToFound.col == i):
                                index+=1
                                if(index >= len(my_coords)):
                                    module_done = False
                                else:
                                    coordToFound = my_coords[index]
                                    print("Good")
                            else:
                                index = 0
                                coordToFound = my_coords[index]
                                print("Fail")

                            # do nothing while button is being held down
                            while(buttons.buttonHeldDown(i)):
                                pass
                    # return each output pin to high
                    GPIO.output(buttons.columnPins[j],1)

    print("ENIGME TERMINEE")

    lcd.clear()
    lcd.message("OK !")