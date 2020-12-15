# Class responsible for managing temperature sensor
from datetime import datetime
import time
#from utils.TempLogger import TempLogger
from w1thermsensor import W1ThermSensor
import json




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
            counter = 0
            info = {}
            #load the temperature measurements/values.
            #loop through sensor values and add to the measurements to the correct id 
            for sensor in W1ThermSensor.get_available_sensors():
                    
                    self.data[sensor.id]["value"] =  str(sensor.get_temperature())
                    self.data[sensor.id]["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    rec ={}                   
                    rec["identifier"] = self.data[sensor.id]["identifier"]
                    rec["value"] = self.data[sensor.id]["value"]
                    rec["location"] = self.data[sensor.id]["location"]
                    
                                  
                    #print(self.data[sensor.id]["name"] + " : " + self.data[sensor.id]["value"]  + " : " + self.data[sensor.id]["location"])
                    print (f"record value : {rec}")
                    info[counter] = rec
                    counter = counter + 1
                    
            print(f'info line 1 {info[0]["value"]}')       
                    
            
            html_object = f"""
                          <!DOCTYPE html>
                            <html>
                            <head>
                            <title>Sensor overview </title>
                            </head>
                            <body>

                            <h1>Sensor overview</h1>
                            <p>{info[0]["value"]} :{info[0]["location"]}  </p>
                            <p>{info[1]["value"]} :{info[1]["location"]}  </p>
                            <p>{info[2]["value"]} :{info[2]["location"]}  </p>
                            <p>{info[3]["value"]} :{info[3]["location"]}  </p>
                            <p>{info[4]["value"]} :{info[4]["location"]}  </p>

                            </body>
                            </html>
                          """
            
            
            return  html_object



    
