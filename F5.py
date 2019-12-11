from constants import lcd, ButtonMatrix, GPIO
from random import seed, randint

seed(1)

my_coords = []

buttons = ButtonMatrix()

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Turn backlight on
lcd.set_backlight(0)

class Coordonnees():
    def __init__(self,row, col):
        self.row = row
        self.col = col
    
    def GetPos(self):
        val = 'A' if self.row == 3 else 'B' if self.row == 2 else 'C' if self.row == 1 else 'D'
        return val + str(self.col)
        #return(self.rowToLetter(self.row)+self.col)

def CreateCode():
    for i in range(5):
        row = randint(0,4)
        col = randint(0,4)
        print("r : " + str(row) + " | c : " + str(col))
        my_coords.append(Coordonnees(row, col))

CreateCode()

code = ""

for co in my_coords:
    print(co.GetPos())

# Print a two line message
lcd.message(code)
    
while(True):
            for j in range(len(buttons.columnPins)):
                # set each output pin to low
                GPIO.output(buttons.columnPins[j],0)
                for i in range(len(buttons.rowPins)):
                    if GPIO.input(buttons.rowPins[i]) == 0:
                        # button pressed, activate it
                        buttons.activateButton(i,j)
                        print("x:" + str(i) + " | y: " + str(j))
                        # do nothing while button is being held down
                        while(buttons.buttonHeldDown(i)):
                            pass
                # return each output pin to high
                GPIO.output(buttons.columnPins[j],1)