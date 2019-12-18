#!/usr/bin/python3

from constants import GPIO,time,LightSensor
import smbus

def Start():
    # Find the right revision for bus driver
    if(GPIO.RPI_REVISION == 1):
        bus = smbus.SMBus(0)
    else:
        bus = smbus.SMBus(1)

    playing = True
    sensor = LightSensor()
    while playing:
        if(sensor.readLight() < 10):
            playing = False
    print("Successfully disarmed")

def Enigme():
    return "La lumière cache parfois la solution"
