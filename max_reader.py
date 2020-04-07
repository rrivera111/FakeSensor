# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
import time
import board
import busio
import digitalio
import adafruit_max31865
# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D5)  # pt1000 - 1 
cs2 = digitalio.DigitalInOut(board.D6)  # pt1000 - 2 

#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor1 = adafruit_max31865.MAX31865(spi, cs1, rtd_nominal=1000, ref_resistor=4300.0, wires=2)
sensor2 = adafruit_max31865.MAX31865(spi, cs2, rtd_nominal=1000, ref_resistor=4300.0, wires=4)

 
# Main loop to print the temperature every second.

def tempreading1() : 
    temp = sensor1.temperature
    # temp = ('{0:0.3f}C'.format(temp))
    # Print the value.
    # print('Temperature: {0:0.3f}C'.format(temp))
    # Delay for a second.
    # time.sleep(1.0)
    # print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
    return (temp)

def tempreading2() : 
    temp = sensor2.temperature
    # temp = ('{0:0.3f}C'.format(temp))
    # Print the value.
    # print('Temperature: {0:0.3f}C'.format(temp))
    # Delay for a second.
    # time.sleep(1.0)
    # print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
    return (temp)
