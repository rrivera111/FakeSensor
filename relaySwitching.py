import os 
import sys 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RelayList = [23,22,4,27,12,17,18,20]
GPIO.setup(RelayList, GPIO.OUT)


class Relay: 
    
    def __init__(self):
       #self.GPIO = GPIO 
       #GPIO.setmode(GPIO.BCM)
       #GPIO.setwarnings(False)
       #RelayList = [23,22,4,27,12,17,18,20]
       #GPIO.setup(RelayList,GPIO.OUT)
       #print("Init print")
       # self.inputPin = inputPin
        pass
       # GPIO.setmode(GPIO.BCM)
       # GPIO.warnings(False)
        #GPIO.setup(self.inputPin,GPIO.OUT)
        #GPIO.output(self.inputPin,GPIO.LOW)
    def ON(self,IN) :
        GPIO.output(IN,GPIO.LOW)
        #GPIO.output(IN,GPIO.LOW)
        time.sleep(1)
        print("relay ON on pin "  )

    def OFF(self,IN):
       
        GPIO.output(IN,GPIO.HIGH)

# Here's our payoff idiom!
if __name__ == '__main__':
    pass

