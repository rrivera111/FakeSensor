import sys, os 
import time 

import paho.mqtt.client as mqtt
import random, threading, json 
from datetime import datetime 

MQTT_Broker = "localhost"
MQTT_Port = 1883 
Keep_Alive_Interval = 45 
MQTT_Topic_Humidity = "Home/Humidity" 
MQTT_Topic_Temperature = "Temperature"

mqttc = mqtt.Client() 
mqttc.connect(MQTT_Broker, int(MQTT_Port),int(Keep_Alive_Interval))
toggle = 0 

def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	#print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	#print ""
	

def publish_Fake_Sensor_Values_to_MQTT(): 
	threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))

		Humidity_Data = {}
		Humidity_Data['Sensor_ID'] = "Dummy-1"
		Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		Humidity_Data['Humidity'] = Humidity_Fake_Value
		humidity_json_data = json.dumps(Humidity_Data)

		#print "Publishing fake Humidity Value: " + str(Humidity_Fake_Value) + "..."
		publish_To_Topic (MQTT_Topic_Humidity, humidity_json_data)
		toggle = 1

	else:
		Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))

		Temperature_Data = {}
		#Temperature_Data['Sensor_ID'] = "Dummy-2"
		#Temperature_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		Temperature_Data['Temperature'] = Temperature_Fake_Value
		temperature_json_data = json.dumps(Temperature_Data)

		print str(temperature_json_data) 
		publish_To_Topic (MQTT_Topic_Temperature, Temperature_Fake_Value) #temperature_json_data

		toggle = 0


publish_Fake_Sensor_Values_to_MQTT()


