#!/usr/bin/python
import relaySwitching_Old 
import time
import RPi.GPIO as GPIO

class relayTest : 
	def __init__ (self) :
		self.relay = relaySwitching_Old.relay()
	
	def triggerRelayON (self) : 
		self.relay.ON(6)
		
	def triggerRelayOFF (self) : 
		self.relay.OFF(6)


try:
    while True:
		my_relay = relaySwitching_Old.relay()
		my_relay2 = relayTest()
		print('Relay on') 
		my_relay.ON(5)
		time.sleep(0.5)
		print('Relay off')
		my_relay.OFF(5)
		time.sleep(0.5)
		my_relay2.triggerRelayON()
		time.sleep(0.5)
		my_relay2.triggerRelayOFF()
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('interrupted!')
