import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import SevenSegment
import Adafruit_CharLCD as LCD

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

        # matrix button ids
        self.buttonIDs = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
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
        print("button " + str(btnIndex + 1) + " pressed")
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

# lcd 
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

# light senseor
class LightSensor():

    def __init__(self):

        # Define some constants from the datasheet

        self.DEVICE = 0x5c # Default device I2C address

        self.POWER_DOWN = 0x00 # No active state
        self.POWER_ON = 0x01 # Power on
        self.RESET = 0x07 # Reset data register value

        # Start measurement at 4lx resolution. Time typically 16ms.
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        # Start measurement at 1lx resolution. Time typically 120ms
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        # Start measurement at 0.5lx resolution. Time typically 120ms
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        # Start measurement at 1lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        # Start measurement at 0.5lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        # Start measurement at 1lx resolution. Time typically 120ms
        # Device is automatically set to Power Down after measurement.
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):

        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)

    def readLight(self):

        data = bus.read_i2c_block_data(self.DEVICE,self.ONE_TIME_HIGH_RES_MODE_1)
        return self.convertToNumber(data)

# matrix

# Touch
touch = 17
