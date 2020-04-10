#!/usr/bin/python
import relaySwitching
import time
import RPi.GPIO as GPIO
my_relay = relaySwitching.relay(5, invert=True)

try:
    while True:
		print('Relay on') 
		my_relay.on()
		time.sleep(1)
		print('Relay off')
		my_relay.off()
		time.sleep(1)


except KeyboardInterrupt:
	GPIO.cleanup()
	print('interrupted!')
