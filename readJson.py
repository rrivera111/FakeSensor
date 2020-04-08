import json
from time import sleep
#import pandas as pd

def readSettings ():
  with open('settings.json') as f:
    data = json.load(f)
    print(type(data))
    #df = pd.DataFrame(data)
    #print(type(df))
    #setpoint1 = data['setpoint1']
    #setpoint2 = data['setpoint2']
    #deltaT    = data['deltaT']
    x1 = data['x1']
    x2 = data['x2']
    x3 = data['x3']
  #return 
  return(x1,x2,x3)

while True :
  read = readSettings() 
  print (read)
  print (type(read))
  sleep(1)


