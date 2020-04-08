# Rev 0 - Function for reading PT 1000 and trigger logic 

import time
import heatingFunctions
import json
from statistics import mean
from datetime import datetime
from datetime import date
#from datetime import time
from datetime import timedelta
import board
import busio
import digitalio
import adafruit_max31865
#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#cs = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board.
#sensor = adafruit_max31865.MAX31865(spi, cs)
#sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=1000, ref_resistor=4300, wires=2)
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
T1_1 = pt1000(5,2)
# PT100 2 definition  , DI 6 wires 4 
T2_1 = pt1000(6,4)
heating = heatingFunctions.heating() 
while True : 
    # just defined for one object since settings are same for both 
    setpoints = T1_1.readSettings() 
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
    heati = heating.function1(x1,x3,x2,x4,T1,T2,setpoint1,setpoint2,deltaT)
    time.sleep(.5)
