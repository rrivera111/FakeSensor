#!/usr/bin/env python
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

class relay:
	def __init__(self, pin, invert=False, init=False ) :
		self._pin = pin
		self.inverted = invert
		self.state = init
		GPIO.setup(self._pin, GPIO.OUT,initial=init^invert) 
	def set_output(self,state):
		self.state = bool(state)
		GPIO.output(self._pin,self.state^self.inverted) 
		
	def on(self):
		self.set_output(True)
	def off(self):
		self.set_output(False)

if __name__ == '__main__':
	try : 
		for i in range(0,8) :
			print('Relay on')
			testRelay = relay(RelayList[i],invert=True)
			testRelay.on()
			time.sleep(0.5)
			testRelay.off()
			print('Relay off')
			time.sleep(0.5)
		GPIO.cleanup()
	
	except:
		GPIO.cleanup()
