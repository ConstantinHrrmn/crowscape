#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Matt Hawkins
# Author's Git: https://bitbucket.org/MattHawkinsUK/
# Author's website: https://www.raspberrypi-spy.co.uk
# http://elecrow.com/
from constants import GPIO,time,LightSensor
import smbus

 # Find the right revision for bus driver
if(GPIO.RPI_REVISION == 1):
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)

playing = True
sensor = LightSensor()
print("La lumière cache parfois la solution")
while playing:
    if(sensor.readLight() < 10):
        playing = False
print("Successfully disarmed")