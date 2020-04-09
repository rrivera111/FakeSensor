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
        #self.GPIO = GPIO 
        #self.GPIO.setmode(GPIO.BCM)
        #self.GPIO.setwarnings(False)
        #RelayList = [23,22,4,27,12,17,18,20]
        #self.GPIO.setup(RelayList,GPIO.OUT)
        #print("Init print")
        #self.inputPin = inputPin
        #GPIO.setup(self.inputPin,GPIO.OUT)
        #GPIO.output(self.inputPin,GPIO.LOW)
        pass
    def ON(self,IN) :
        GPIO.output(IN,GPIO.LOW)
        #GPIO.output(IN,GPIO.LOW)
        #time.sleep(1)
        print("relay ON on pin "  )
    def OFF(self,IN):
        GPIO.output(IN,GPIO.HIGH)

if __name__ == '__main__':
    #Relay.OFF(23)
    test = Relay()
    test.OFF(23)
    test.ON(22)
    test.ON(4)
    time.sleep(1)	
    GPIO.cleanup()
    #test.OFF(23)
    #pass

