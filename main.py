#!/usr/bin/env python3
# Rev 0 - Function for reading PT 1000 and trigger logic 
# Import general libraries
import sys, os 
import time
import random, threading, json 
from statistics import mean
from datetime import datetime
from datetime import date
#from datetime import time
from datetime import timedelta
# MQTT client
import paho.mqtt.client as mqtt
# imports heating functions 
import heatingFunctions
import board
import busio
import digitalio
import adafruit_max31865

MQTT_Broker = "localhost"
MQTT_Port = 1883 
Keep_Alive_Interval = 45 
MQTT_Topic_Boiler = "Boiler" 
MQTT_Topic_Heater = "Heater"

mqttc = mqtt.Client() 
mqttc.connect(MQTT_Broker, int(MQTT_Port),int(Keep_Alive_Interval))
toggle = 0 

# heating  Functions 
counter = 0 
temp_avg = []
start = datetime.now()
class pt1000 :
    def __init__(self,boardPin,wires):
        self.spi = busio.SPI(board.SCK,MOSI=board.MOSI,MISO=board.MISO)
        self.wires =  wires
        if boardPin == 5:
            self.boardPin =  digitalio.DigitalInOut(board.D5)
        elif boardPin == 6:
            self.boardPin =  digitalio.DigitalInOut(board.D6)
    def tempreading(self) : 
        sensor = adafruit_max31865.MAX31865(self.spi,self.boardPin,rtd_nominal=1000,ref_resistor=4300,wires=self.wires)
        while True :
            global start
            current = datetime.now()
            timer = current - start
            tDelta = timedelta(seconds=5)
            if timer < tDelta : 
                global counter
                global temp_avg
                counter =+ 1  
                temp = sensor.temperature
                temp_avg.append(temp)
            elif timer > tDelta : 
                counter = 0 
                start = datetime.now()
                if temp_avg == [] :
                    tempMean =  sensor.temperature
                else:
                    tempMean = mean(temp_avg)
                #print(temp_avg)
                tempMean = round(tempMean,2)
                #print(type('Mean Temperature 1: {0:0.3f}C'.format(tempMean)))
                temp_avg = []
                #print(temp_avg)
                time.sleep(.5)
                return (tempMean)
    def readSettings (self):
        with open('settings.json') as f:
            data = json.load(f)
            setpoint1 = data['setpoint1']
            setpoint2 = data['setpoint2']
            deltaT    = data['deltaT']
            x1 = data['x1']
            x2 = data['x2']
            x3 = data['x3']
            x4 = data['x4']
        return(setpoint1,setpoint2,deltaT,x1,x2,x3,x4)
# PT100 1 definition , DI 5 wires 2  
T1_1 = pt1000(5,4)
# PT100 2 definition  , DI 6 wires 4 
T2_1 = pt1000(6,4)
heating = heatingFunctions.heating() 


# MQTT functions 
# Publush to topic 
sensor1 = T1_1
sensor2 = T2_1
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
# Gathers sensor data and publush to defined topics 
def publish_Sensor_Values_to_MQTT(): 
	threading.Timer(3.0, publish_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		valueSensor1 = str(sensor1)      
		#valueSensor1 = float("{0:.2f}".format(sensor1))
		#valueSensor1_Data = {}
		#valueSensor1_json_data = json.dumps(valueSensor1_Data)
		publish_To_Topic (MQTT_Topic_Boiler, valueSensor1)
		toggle = 1
	else:
		valueSensor2 = str(sensor2)       
		#valueSensor2 = float("{0:.2f}".format(sensor2))
		#valueSensor2_Data = {}
		#valueSensor2_json_data = json.dumps(valueSensor2_Data)
		#print str(temperature_json_data) 
		publish_To_Topic (MQTT_Topic_Heater, valueSensor2)
		toggle = 0
#publish_Sensor_Values_to_MQTT()

try : 
    while True : 
        # just defined for one object since settings are same for both 
        setpoints = T1_1.readSettings() 
        # parsing settings from readingficntion class pt1000 (main)
        setpoint1 = setpoints[0] 
        setpoint2 = setpoints[1] 
        deltaT = setpoints[2] 
        x1 = setpoints[3]
        x2 = setpoints[4]
        x3 = setpoints[5]
        x4 =setpoints[6]
        T1 = T1_1.tempreading()
        print("Temperature T1 : " + str(T1))		
        T2 = T2_1.tempreading()
        print("Temperature T2 : " + str(T2))
        heating.function1(x1,x3,x2,x4,T1,T2,setpoint1,setpoint2,deltaT)
        time.sleep(.5)
        publish_Sensor_Values_to_MQTT()

except KeyboardInterrupt : 
    GPIO.cleanup()
    print('interrupted!')



