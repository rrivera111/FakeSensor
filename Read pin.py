#!/usr/bin/env python3
import json
import RPi.GPIO as GPIO
from openhab import openHAB
import random, threading, json
from time import sleep
## Virtual switch definition 
#base_url =  'http://localhost:8080/rest'
#openhab = openHAB(base_url)
#items=openhab.fetch_all_items()
#switch1Vritual = items.get('channel4') 
#switch1Vritual = switch1Vritual.state

## GPIO Read outs 
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#settings = {
#    'setpoint1': 21,
#    'setpoint2':31,
#    'deltaT':1,
#    'x1':1, # heating on
#    'x2':1, # warm water
#    'x3':1, # sommer time
#    'x4':1 # winter time
#}

def inputs(pin1):
    input1 = GPIO.input(pin1)
    if input1 == 1 :
        val = 1 
    else :
        val = 0
    return val 

def inputVirtual(virtualSwitch):
    input = virtualSwitch
    if input == "ON" :
        val = 1 
    else :
        val = 0
    return val 

while True : 

    value1 = GPIO.input(13)#inputs(13)
    value2 = GPIO.input(26)#inputs(26)
    print (value1)
    print (value2)
    sleep(1)

