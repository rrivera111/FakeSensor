from openhab import openHAB
import time
import os
import pdb
import datetime
import RPi.GPIO as GPIO
import time
Room1 = 12 # Room "" Y5  rel 12
Room2 = 17 # Room "" Y6  rel 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(Room1,GPIO.OUT)
#GPIO.setup(Room2,GPIO.OUT)
base_url =  'http://localhost:8080/rest'
openhab = openHAB(base_url)
items=openhab.fetch_all_items()
channel =items.get('channel4')
#tempRomm1 = items.get('Temperature')  # Name ??
#set_point1 = items.get('Setpoint')    # Room1 Set point
#tempRomm2  = items.get('Temperature') # Name ??
#set_point2 = items.get('Setpoint')    # Room1 Set point

def HeatOn(Room):
	GPIO.output(Room,GPIO.LOW)
def HeatOff(Room):
	GPIO.output(Room,GPIO.HIGH)
#while 1 : 
#	if tempRomm1.state > set_point1.state:
#		HeatOn(Room1)
#	else:
#		HeatOff(Room1)
#	if tempRomm2.state > set_point2.state:
#		HeatOn(Room2)
#	else:
#		HeatOff(Room2)
	
#print(items)
#Checking temp Room1 
print("Checking temp Room1") 
print(items)
print(channel.state)
#print("Checking temp Room2") 
#print(tempRomm2)
time.sleep(1)
