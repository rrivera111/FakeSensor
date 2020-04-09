#!/usr/bin/env python3
# import general libraries
import time
import os 
import sys 
# GPIO Library
import RPi.GPIO as GPIO
# GPIO definitions
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# relays definition 
RelayList = [23,22,4,27,12,17,18,20]
# GPIO pins defined as ouputs
GPIO.setup(RelayList, GPIO.OUT)
class Relay: 
    def __init__(self):
        pass
    def ON(self,IN) :
        GPIO.output(IN,GPIO.LOW)
        GPIO.cleanup()
    def OFF(self,IN):
        GPIO.output(IN,GPIO.HIGH)
        GPIO.cleanup()
if __name__ == '__main__':
    print(len(RelayList))
    #Relay.OFF(23)
    #testRelay = Relay()
    for i in RelayList :
        print(RelayList[i])
    #    testRelay.ON(RelayList[i])
    #    time.sleep(.5)
    #for i in RelayList : 
    #    testRelay.OFF(RelayList[i])
    #    time.sleep(.5)

    time.sleep(1)
