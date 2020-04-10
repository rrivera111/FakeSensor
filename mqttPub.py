#!/usr/bin/env python3
import sys, os 
import time 
import paho.mqtt.client as mqtt
import random, threading, json 
from datetime import datetime 
import max_reader

MQTT_Broker = "localhost"
MQTT_Port = 1883 
Keep_Alive_Interval = 45 
MQTT_Topic_Boiler = "Boiler" 
MQTT_Topic_Heater = "Heater"

mqttc = mqtt.Client() 
mqttc.connect(MQTT_Broker, int(MQTT_Port),int(Keep_Alive_Interval))
toggle = 0 
# PT 1000 definition 

sensor1 = max_reader.tempreading1()
sensor2 = max_reader.tempreading2()

# Functions 
# Publush to topic 
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)

# Gathers sensor data and publush to defined topics 
def publish_Fake_Sensor_Values_to_MQTT(): 
	#threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		valueSensor1 = float("{0:.2f}".format(sensor1))
		valueSensor1_Data = {}
		valueSensor1_json_data = json.dumps(valueSensor1_Data)
		publish_To_Topic (MQTT_Topic_Boiler, valueSensor1)
		toggle = 1
	else:
		valueSensor2 = float("{0:.2f}".format(sensor2))
		valueSensor2_Data = {}
		valueSensor2_json_data = json.dumps(valueSensor2_Data)
		#print str(temperature_json_data) 
		publish_To_Topic (MQTT_Topic_Heater, valueSensor2)
		toggle = 0

while True : 
	publish_Fake_Sensor_Values_to_MQTT()
	time.sleep(.5)



