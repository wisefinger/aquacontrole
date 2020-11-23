# Class responsible for managing temperature sensor
from datetime import datetime
import time
#from utils.TempLogger import TempLogger
from w1thermsensor import W1ThermSensor
import json
from json2html import *




class TempSensor:
    
    #templogger = TempLogger()

    def __init__(self):
        # def dictonary to reply da
        self.data = {}
        
        # load sensor meta-data
        self.sensors = {
           "0517a2b17bff"  : {
                "identifier"   : "0517a2b17bff",
                "name" : "temp5",
                "type" : "temperature",
                "location" : "discus rek onder",
                "units" : "Celcius"
              },
           "0220104528b1" : {
                "identifier"   : "0220104528b1",
                "name" : "temp3",
                "type" : "temperature",
                "location" : "aging barrel",
                "units" : "Celcius"
              },
             "0301a279830b": {
                "identifier"   : "0301a279830b", 
                "name" : "temp4",
                "type" : "temperature",
                "location" : "discus rek boven",
                "units" : "Celcius"
              },
             "0301a279ec7d": {
                "identifier"   : "0301a279ec7d",
                "name" : "temp1",
                "type" : "temperature",
                "location" : "breeding tank",
                "units" : "Celcius"
              },
              "0301a2793e33" : {
                "identifier"   : "0301a2793e33",
                "name" : "temp2",
                "type" : "temperature",
                "location" : "quarantaine tank",
                "units" : "Celcius"
            }
        }

    def getAllTempJson(self):

            # load ref data sensors and add to new records
            for key,val in self.sensors.items():
                record = {}
                record["identifier"] = val.get('identifier')
                record["name"] = val.get('name')
                record["type"] = val.get('type')
                record["location"] = val.get('location')
                record["units"] = val.get('units')
                self.data[key] = record    
         
            #load the temperature measurements/values.
            #loop through sensor values and add to the measurements to the correct id 
            for sensor in W1ThermSensor.get_available_sensors():
                    self.data[sensor.id]["value"] =  str(sensor.get_temperature())
                    self.data[sensor.id]["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                 
            # Serializing json    
            json_object = json.dumps(self.data, indent = 4)   
            #print(json_object)              
            return  json_object

    def getAllTempHtml(self):

            # load ref data sensors and add to new records
            for key,val in self.sensors.items():
                record = {}
                record["identifier"] = val.get('identifier')
                record["name"] = val.get('name')
                record["type"] = val.get('type')
                record["location"] = val.get('location')
                record["units"] = val.get('units')
                self.data[key] = record    
         
            #load the temperature measurements/values.
            #loop through sensor values and add to the measurements to the correct id 
            for sensor in W1ThermSensor.get_available_sensors():
                    self.data[sensor.id]["value"] =  str(sensor.get_temperature())
                    self.data[sensor.id]["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                 
            # Serializing json    
            json_object = json.dumps(self.data, indent = 4)   
            #print(json_object)
            
            return  json2html.convert(json = json_object)



    
