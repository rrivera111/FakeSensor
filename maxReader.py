import time
from statistics import mean
from datetime import datetime
from datetime import date
#from datetime import time
from datetime import timedelta
import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board.

cs2 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.

#sensor = adafruit_max31865.MAX31865(spi, cs)
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=1000, ref_resistor=4300, wires=2)

#sensor2 = adafruit_max31865.MAX31865(spi, cs2)
sensor2 = adafruit_max31865.MAX31865(spi, cs2, rtd_nominal=1000, ref_resistor=4300, wires=4)


counter = 0 
temp_avg = []

counter2 = 0 
temp_avg2 = [] 

start = datetime.now()
start2 = datetime.now()


class pt1000 :
    def tempreading(self,dIO,wires) : 
        cs
        #timeHist = 5.0 
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
                tempMean = mean(temp_avg)
                print(temp_avg)
                print('Mean Temperature 1: {0:0.3f}C'.format(tempMean))
                temp_avg = []
                print(temp_avg)
                time.sleep(3)
                return (tempMean)

    def tempreading2(self) : 
        
        #timeHist = 5.0 
        while True :
            global start2
            current = datetime.now()
            timer = current - start
            tDelta = timedelta(seconds=5)
            if timer < tDelta : 
                global counter2
                global temp_avg2
                counter2 =+ 1  
                temp = sensor2.temperature
                temp_avg2.append(temp)
            elif timer > tDelta : 
                counter2 = 0 
                start2 = datetime.now()
                tempMean2 = mean(temp_avg2)
                print(temp_avg2)
                print('Mean Temperature 2: {0:0.3f}C'.format(tempMean2))
                temp_avg2 = []
                print(temp_avg2)
                time.sleep(3)
                return (tempMean2)

testT1 = pt1000()
testT2 = pt1000()
while True : 
    testT1.tempreading()	
    testT2.tempreading2()
