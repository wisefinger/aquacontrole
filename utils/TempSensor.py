# Class responsible for managing temperature sensor
from datetime import datetime
import time
from utils.TempLogger import TempLogger
from w1thermsensor import W1ThermSensor



class TempSensor:
    
    templogger = TempLogger()

    def __init__(self):
        # def dictonary to reply da
        self.data = {}
        
        # load sensor meta-data
        self.sensors = {
            "0301a2793e33" : {        
                "name" : "temp5",
                "type" : "temperature",
                "location" : "discus rek onder",
                "units" : "°Celcius"
              },
            "0301a279ec7d" : {
                "name" : "temp3",
                "type" : "temperature",
                "location" : "aging barrel",
                "units" : "°Celcius"
              },
             "0220104528b1" : {
                "name" : "temp4",
                "type" : "temperature",
                "location" : "discus rek boven",
                "units" : "°Celcius"
              },
             "0517a2b17bff" : {
                "name" : "temp1",
                "type" : "temperature",
                "location" : "breeding tank",
                "units" : "°Celcius"
              },
              "0301a279830b" : {
                "name" : "temp2",
                "type" : "temperature",
                "location" : "quarantaine tank",
                "units" : "°Celcius"
            }
        }

    def getTemp(self):

        
        for key,val in self.sensors.items():
            record = {}
            record["name"] = val.get('name')
            record["type"] = val.get('type')
            record["location"] = val.get('location')
            record["units"] = val.get('units') 
            self.data[key] = record
            
            
        #load the temperature measurements/values
        for sensor in W1ThermSensor.get_available_sensors():
            self.data[sensor.id]["value"] =  sensor.get_temperature()
            self.data[sensor.id]["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
       
        return  self.data




    
