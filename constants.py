import RPi.GPIO as GPIO
import time
import smbus
from Adafruit_LED_Backpack import SevenSegment
import Adafruit_CharLCD as LCD
import Adafruit_DHT

# single red led
led_pin = 26

# Green buttons 
gb_up = 37
gb_down = 33
gb_left = 22
gb_right = 35

# yellow buttons 
class ButtonMatrix():

    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        # matrix button ids [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        self.buttonIDs = [[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]]
        # gpio inputs for rows
        self.rowPins = [27,22,5,6]
        # gpio outputs for columns
        self.columnPins = [13,19,26,25]

        # define four inputs with pull up resistor
        for i in range(len(self.rowPins)):
            GPIO.setup(self.rowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # define four outputs and set to high
        for j in range(len(self.columnPins)):
            GPIO.setup(self.columnPins[j], GPIO.OUT)
            GPIO.output(self.columnPins[j], 1)

    def activateButton(self, rowPin, colPin):
        # get the button index
        btnIndex = self.buttonIDs[rowPin][colPin] - 1
        #print("button " + str(btnIndex + 1) + " pressed")
        # prevent button presses too close together
        time.sleep(.3)

    def buttonHeldDown(self,pin):
        if(GPIO.input(self.rowPins[pin]) == 0):
            return True
        return False

# seven segments 
sev_seg = SevenSegment.SevenSegment(address=0x70)

# buzzer 
buzzer = 13

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

# matrix

# Touch
touch = 17

#temperature / humidity
temp = 4
temp_sensor_type = 11
