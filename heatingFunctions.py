# Main heating functions for Dietmars Heating plant 
from openhab import openHAB
import time 
import os
import pdb
import datetime
import RPi.GPIO as GPIO
import time
import sys 
import relaySwitching
Rel1 = 23 #y1
Rel2 = 22 #y2
Rel3 = 4  #y3
Rel4 = 27 #y4
#Rel5 = 12 #y5
#Rel6 = 17 #y6
#Rel7 = 18 #y7
#Rel8 = 20 #y8
#Relay = [1,2,3,4,5,6,7,8] # Relays mapping list
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(Relay,GPIO.OUT)
# args, x4 and x3 
# sys.argv[1]-T1,sys.argv[2]-T2, T5,T6 
# Heating functions 
# variables definition 
# x1= heating , x2= warm water  ,x3= sommer ,x4= winter
#
class heating : 
    def __init__ (self) :
        base_url =  'http://localhost:8080/rest'
        openhab = openHAB(base_url)
        items=openhab.fetch_all_items()
        self.temp = items.get('Temperature')
        self.set_point = items.get('Setpoint')
        self.relay = relaySwitching.Relay()
    def relay1(self,relay,onoff) : 
        if onoff == 1:
            #GPIO.output(relay,GPIO.LOW)
            print("Relay " + str(relay)+ " ON")
        else :
            #GPIO.output(relay,GPIO.HIGH)
            print("Relay " + str(relay)+ " OFF")

    def function1 (self,x1,x3,x2,x4,T1,T2,setpoint1, setpoint2,delta1):
        #relay = relaySwitching.Relay()
        # condition1 , out = y3
        #setpoint1 = 40
        #setpoint2 = 50 
        if x3 ==1 : # summer time 
            if x1 == 1 : # heating on 
                if T2 > setpoint1  and T2 < setpoint2 : #y3
                    #relay(Relay[2],1)
                    # # relay on
                    # #GPIO.output(Relay[2],GPIO.LOW)
                    # # relay off
                    # #GPIO.output(Relay[0],GPIO.HIGH)
                    # #GPIO.output(Relay[1],GPIO.HIGH)
                    # #GPIO.output(Relay[3],GPIO.HIGH) 
                    self.relay.ON(Rel3)
                    self.relay.OFF(Rel1)
                    self.relay.OFF(Rel2)
                    self.relay.OFF(Rel4)
                    #relay.OFF(Rel5)
                    #relay.OFF(Rel6)
                    print("condition 1 ON")
                if T2 > setpoint2 :  #y2
                    # relay on 
                    # # #GPIO.output(Relay[1],GPIO.LOW)
                    # # # relay off
                    # #GPIO.output(Relay[0],GPIO.HIGH)
                    # #GPIO.output(Relay[2],GPIO.HIGH)
                    # #GPIO.output(Relay[3],GPIO.HIGH)
                    self.relay.ON(Rel2)
                    self.relay.OFF(Rel1)
                    self.relay.OFF(Rel3)
                    self.relay.OFF(Rel4)
                    #relay.OFF(Rel5)
                    #relay.OFF(Rel6)
                    print("condition 2 ON") 
            if x1 == 0 :  # warm water 
                if T2 > setpoint2 :  #y4 and y1
                    # relay on 
                    # # #GPIO.output(Relay[1],GPIO.LOW)
                    # # # relay off
                    # #GPIO.output(Relay[0],GPIO.HIGH)
                    # #GPIO.output(Relay[2],GPIO.HIGH)
                    # #GPIO.output(Relay[3],GPIO.HIGH)
                    self.relay.ON(Rel1)
                    self.relay.ON(Rel4)
                    self.relay.OFF(Rel2)
                    self.relay.OFF(Rel3)
                    #relay.OFF(Rel5)
                    #relay.OFF(Rel6)
                    print("condition 3 ON") 
        if x3 ==0 : # winter time
            if x1 == 0 :  # warm water 
                if T2 > setpoint1 :  #y4 and y1
                    # relay on 
                    # # #GPIO.output(Relay[1],GPIO.LOW)
                    # # # relay off
                    # #GPIO.output(Relay[0],GPIO.HIGH)
                    # #GPIO.output(Relay[2],GPIO.HIGH)
                    # #GPIO.output(Relay[3],GPIO.HIGH)
                    self.relay.ON(Rel1)
                    self.relay.ON(Rel4)
                    self.relay.OFF(Rel2)
                    self.relay.OFF(Rel3)
                    #relay.OFF(Rel5)
                    #relay.OFF(Rel6)
                    print("condition 4 ON") 
                if T2 > T1 + delta1 :  #y2
                    # relay on 
                    # # #GPIO.output(Relay[1],GPIO.LOW)
                    # # # relay off
                    # #GPIO.output(Relay[0],GPIO.HIGH)
                    # #GPIO.output(Relay[2],GPIO.HIGH)
                    # #GPIO.output(Relay[3],GPIO.HIGH)
                    self.relay.ON(Rel2)
                    self.relay.ON(Rel1)
                    self.relay.OFF(Rel3)
                    self.relay.OFF(Rel4)
                    #relay.OFF(Rel5)
                    #relay.OFF(Rel6)
                    print("condition 5 ON") 

            else :
                print ("Else")    
    def function2 (self,Relay) :
        if self.temp.state > self.set_point.state :
            self.relay.ON(Relay)
        else :
            self.relay.OFF(Relay)

if __name__ == '__main__':
    pass

#heating = heating () 
# test function 
#heating.function1(int(sys.argv[1]),int(sys.argv[2]),1,1,int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[7]),int(sys.argv[7]))
# mapping 
#args = sys.argv
#heating.function1(int(sys.argv[1]),int(sys.argv[2]),1,1,int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[7]),int(sys.argv[7]))
