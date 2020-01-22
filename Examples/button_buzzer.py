#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# configure both button and buzzer pins
button_pin = 35
buzzer_pin = 13

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

i=0

try:
    while True:
        # check if button pressed
        print(GPIO.input(button_pin))
        if(GPIO.input(button_pin) == 0):
            # set buzzer on
            print("bip")
            #GPIO.output(buzzer_pin, GPIO.HIGH)
        else:
            # it's not pressed, set button off
            #GPIO.output(buzzer_pin, GPIO.LOW)
            i = i +1
except KeyboardInterrupt:
    GPIO.cleanup()
