import json

def readSettings ():
  with open('settings.json') as f:
    data = json.load(f)
    setpoint1 = data['setpoint1']
    setpoint2 = data['setpoint2']
    deltaT    = data['deltaT']
  return(setpoint1,setpoint2,deltaT)




