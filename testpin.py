#!/usr/bin/python3
import sys 
import os
import flask
from flask import Flask,jsonify
from flask import Flask, request, render_template
from time import sleep
#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.register_read_message import ReadInputRegistersResponse

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#### Pin definition ##### 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def check_ping():
	host = " 192.168.2.104"
	ping = os.system("ping -c 1" + host)
	if ping == 0 : 
		status = "Alive"
	else:
		status = "Not online"
	return status

def check_ups1():
	#### Pin definition ##### 
	var = GPIO.input(13)
	print(var)
	return var

def check_ups2():
	#### Pin definition ##### 
	var = GPIO.input(26) # alarma
	print(var)
	return var



while True : 
	check_ups1()
	check_ups2()
