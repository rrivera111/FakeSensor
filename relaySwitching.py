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
#RelayList = [23,22,4,27,12,17,18,20]
RelayList = [5, 6, 13, 16, 19, 20, 21, 26] # Original distribution board
# GPIO pins defined as ouputs
GPIO.setup(RelayList, GPIO.OUT)
class relay:
	def __init__(self, pin) #, invert=False, init=False):
		self._pin = pin
		#self.inverted = invert
		#self.state = init
		GPIO.setup(self._pin, GPIO.OUT) #,initial=init^invert) # 
	def set_output(self,state):
		self.state = bool(state)
		GPIO.output(self._pin,self.state)
	def on(self):
		self.set_output(True)
	def off(self):
		self.set_output(False)
#class Relay: 
#    def __init__(self):
#        pass
#    def ON(self,IN) :
#        GPIO.output(IN,GPIO.LOW)
#        GPIO.cleanup()
#    def OFF(self,IN):
#        GPIO.output(IN,GPIO.HIGH)
#        GPIO.cleanup()
if __name__ == '__main__':
    print(len(RelayList))
    #Relay.OFF(23)
    for i in range(0,2) :
        testRelay = relay(RelayList[i])
        testRelay.on()
        time.slepp(0.5)
        #testRelay = relay(RelayList[i])
        testRelay.off()
        print(RelayList[i])
    #    testRelay.ON(RelayList[i])
    #    time.sleep(.5)
    #for i in RelayList : 
    #    testRelay.OFF(RelayList[i])
    #    time.sleep(.5)
