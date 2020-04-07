import json

def readSettings ():
  with open('settings.json') as f:
    data = json.load(f)
    #setpoint1 = data['setpoint1']
    #setpoint2 = data['setpoint2']
    #deltaT    = data['deltaT']
    x1 = data['x1']
    x2 = data['x2']
    x3 = data['x3']

  return(x1,x2,x3)


read = readSettings() 

print read 


