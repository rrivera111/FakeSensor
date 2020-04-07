import json
#import pandas as pd

def readSettings ():
  with open('settings.json') as f:
    data = json.load(f)
    print(type(data))
    df = pd.DataFrame(data)
    print(type(df))
    #setpoint1 = data['setpoint1']
    #setpoint2 = data['setpoint2']
    #deltaT    = data['deltaT']
    x1 = data[0]
    #x2 = data[1]
   # x3 = data[2]
  return df
  #return(x1,x2,x3)
  
read = readSettings() 

print (read)
print (type(read))


