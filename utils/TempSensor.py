# Class responsible for managing temperature sensor
from datetime import datetime
import time
from utils.TempLogger import TempLogger
from w1thermsensor import W1ThermSensor



class TempSensor:
    templogger = TempLogger()

    def __init__(self,name):
        self.name = name
        self.data = {}

    def getTemp(self):
        sensor = W1ThermSensor()
        temperature = sensor.get_temperature()
        # print("The temperature is %s °C" % temperature)
        #self.templogger.log(temperature)
        self.data["sensorid"] = self.name
        self.data["unit"] = "Celcius"
        self.data["value"] = temperature
        self.data["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.templogger.log(self.data)
        return  self.data

    def close(self):
        GPIO.cleanup()

  