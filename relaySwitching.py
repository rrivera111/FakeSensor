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
#Rel1 = 23 #y1
#Rel2 = 22 #y2
#Rel3 = 4  #y3
#Rel4 = 27 #y4
class Relay:
	def __init__(self,  invert=True, init=False ) :
		#self._pin = [5, 6, 13, 16, 19, 20, 21, 26]
		self._pin = [23,22,4,27]
		self.inverted = invert
		self.state = init
		GPIO.setup(self._pin, GPIO.OUT,initial=init^invert) 
	def ON(self,pin):
		self.state = bool(True)
		GPIO.output(pin,self.state^self.inverted) 
		print('Relay on')
	def OFF(self,pin):
		self.state = bool(False)
		GPIO.output(pin,self.state^self.inverted) 
		print('Relay off')

if __name__ == '__main__':
	try : 
		for i in range(0,8) :
			print('Relay on')
			testRelay = relay()
			testRelay.ON(RelayList[i])
			time.sleep(0.5)
			testRelay.OFF(RelayList[i])
			print('Relay off')
			time.sleep(0.5)
		GPIO.cleanup()
	
	except:
		GPIO.cleanup()
